# -*- coding: utf-8 -*-
"""把 880 做题本 content_list 重建成结构化题库 questions.json（v2：段内切题）"""
import json, re
from collections import Counter

FILES = [('高数篇.json', '高等数学'), ('线概篇.json', '线性代数与概率统计')]
CHAPTER_RE = re.compile(r'^第([一二三四五六七八九十百零]+)章\s*(.*)$')
MARK_RE = re.compile(r'[（(]\s*(\d{1,2})\s*[)）]')          # 题号 (1)（1）
ROMAN_RE = re.compile(r'^\s*[（(]?\s*(I{1,3}|IV|VI{0,3}|IX|XI{0,3}|i{1,3}|iv|vi{0,3}|ix|xi{0,3}|[①②③④⑤⑥⑦⑧⑨⑩])\s*[)）]?')
OPT_RE = re.compile(r'^\s*[A-DＡ-Ｄ][\.．、,，]')
TIER_WORDS = {'基础题', '综合题', '拓展题'}
SUBJ_OF_PIAN = {'高等数学篇': '高等数学', '线性代数篇': '线性代数', '概率论与数理统计篇': '概率统计'}
TYPE_KW = [('选择题', '选择题'), ('填空题', '填空题'), ('解答题', '解答题')]

def cn_to_int(s):
    dig = {'零':0,'一':1,'二':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9}
    if s == '十': return 10
    if '十' in s:
        a,_,b = s.partition('十')
        return (dig.get(a,1) if a else 1)*10 + (dig.get(b,0) if b else 0)
    return dig.get(s,0)

def text_of(content_list):
    return ''.join(x.get('content','') for x in content_list if x.get('type')=='text')

def parse(path, default_subject):
    d = json.load(open(path))
    flow = [(pi, blk) for pi, page in enumerate(d) for blk in page]
    st = dict(pian=None, ch=None, chNo=None, kp=None, tier=None, qtype=None)
    Q = []
    cur = None
    expected = 1

    def new_q(no, pi):
        return dict(subject=st['pian'] or default_subject, chapter=st['ch'],
                    chapterNo=st['chNo'], kp=st['kp'], tier=st['tier'],
                    qtype=st['qtype'], localNo=no, page=pi, segs=[])

    def flush():
        nonlocal cur
        if cur is None: return
        has_text = any(k=='text' and v.strip() for k,v in cur['segs'])
        has_math = any(k in ('inline','display','table') for k,v in cur['segs'])
        if has_text or has_math:
            # 清理首尾空白段
            Q.append(cur)
        cur = None

    def ensure_cur(pi):
        """编号模式下取当前题；若还没有，则按 expected 立题（兼容首题以公式开头）"""
        nonlocal cur, expected
        if cur is None:
            cur = new_q(expected, pi); expected += 1
        return cur

    def append_text_with_split(text, pi):
        """在编号模式下，按顺序题号把 text 切开并分派到不同题"""
        nonlocal cur, expected
        idx = 0
        for m in MARK_RE.finditer(text):
            n = int(m.group(1))
            if n == expected:
                before = text[idx:m.start()]
                if before:
                    ensure_cur(pi)['segs'].append(('text', before))
                flush()
                cur = new_q(expected, pi)
                expected += 1
                idx = m.end()
        rest = text[idx:]
        if rest:
            ensure_cur(pi)['segs'].append(('text', rest))

    for pi, blk in flow:
        t = blk['type']; c = blk.get('content', {})
        if t == 'title':
            txt = text_of(c['title_content']).strip()
            mch = CHAPTER_RE.match(txt)
            if txt.endswith('篇'):
                flush(); st['pian'] = SUBJ_OF_PIAN.get(txt, txt); continue
            if mch:
                flush(); st['ch'] = (mch.group(2).strip() or txt); st['chNo'] = cn_to_int(mch.group(1))
                st['tier']=None; st['qtype']=None; expected=1; continue
            if txt in TIER_WORDS:
                flush(); st['tier']=txt; st['qtype']=None; expected=1; continue
            for kw,name in TYPE_KW:
                if kw in txt:
                    flush(); st['qtype']=name; expected=1; break
            continue
        if t == 'page_header':
            txt = text_of(c['page_header_content'])
            if '·' in txt:
                kp = re.sub(r'^\d+\.\s*','',txt.split('·',1)[1].strip())
                if kp: st['kp']=kp
            continue
        if t == 'page_number':
            continue
        if t == 'paragraph':
            pseg = [( 'inline' if x.get('type')=='equation_inline' else 'text'
                      , x.get('content',''))
                     for x in c['paragraph_content'] if x.get('type') in ('text','equation_inline')]
            plain = ''.join(v for k,v in pseg if k=='text').strip()
            # 段落其实是难度/题型标题（PDF 解析偶发把标题归为段落）
            if plain in TIER_WORDS:
                flush(); st['tier']=plain; st['qtype']=None; expected=1; continue
            if plain in ('选择题','填空题','解答题'):
                flush(); st['qtype']=plain; expected=1; continue
            # 统一按顺序题号切分（基础/综合/拓展均用 (1)(2) 编号，(I)(II) 为子问）
            if cur is not None and cur['segs']:
                cur['segs'].append(('text','\n'))
            for k,v in pseg:
                if k=='inline':
                    ensure_cur(pi)['segs'].append(('inline', v))
                else:
                    append_text_with_split(v, pi)
            continue
        if t in ('equation_interline','table','image'):
            ensure_cur(pi)
            if t=='equation_interline': cur['segs'].append(('display', c.get('math_content','')))
            elif t=='table': cur['segs'].append(('table', c.get('html','')))
            else: cur['segs'].append(('text','【题图】'))
            continue
    flush()
    return Q

allq=[]
for f,s in FILES:
    qs=parse(f,s); allq.extend(qs); print(f,'->',len(qs))
print('TOTAL:',len(allq))

# 校验：每个 (科目,章,难度,题型) 内编号是否连续 1..N
groups={}
for q in allq:
    key=(q['subject'],q['chapterNo'],q['tier'],q['qtype'])
    groups.setdefault(key,[]).append(q['localNo'])
bad=0
for key,nums in groups.items():
    exp=list(range(1,len(nums)+1))
    if nums!=exp:
        bad+=1
        if bad<=15: print('SEQ ANOMALY',key,'got',nums)
print('groups:',len(groups),'anomaly groups:',bad)
miss=Counter()
for q in allq:
    for k in ('subject','chapter','tier','qtype'):
        if not q[k]: miss[k]+=1
    if q['localNo'] is None: miss['noNo']+=1
print('missing:',dict(miss))
print('tier:',dict(Counter(q['tier'] for q in allq)))
print('qtype:',dict(Counter(q['qtype'] for q in allq)))
json.dump(allq, open('questions.json','w'), ensure_ascii=False)
print('saved questions.json size', len(json.dumps(allq,ensure_ascii=False)))

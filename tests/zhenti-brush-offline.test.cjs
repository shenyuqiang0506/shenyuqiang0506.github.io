const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const { join } = require('node:path');
const { test } = require('node:test');
const vm = require('node:vm');

const html = readFileSync(join(__dirname, '../zhenti-brush-offline.html'), 'utf8');
const scripts = [...html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/g)];
const bank = JSON.parse(scripts.find((script) => script[1].includes('BANK_DATA'))[2]);
const app = scripts[scripts.length - 1][2];
const chapterId = '高等数学::曲线积分与曲面积分';
const tags = ['第一类曲线积分', '第二类曲线积分', '第一类曲面积分', '第二类曲面积分'];

function start() {
  const elements = new Map();
  const storage = new Map();
  for (const match of html.matchAll(/\bid="([^"]+)"/g)) {
    elements.set(match[1], {
      value: '', textContent: '', innerHTML: '', style: {}, listeners: {},
      addEventListener(event, handler) { this.listeners[event] = handler; }
    });
  }
  elements.get('BANK_DATA').textContent = JSON.stringify(bank);
  vm.runInNewContext(app, {
    setTimeout,
    clearTimeout,
    document: {
      getElementById: (id) => elements.get(id),
      documentElement: { setAttribute() {} }
    },
    window: {},
    localStorage: {
      getItem: (key) => storage.get(key),
      setItem: (key, value) => storage.set(key, value)
    }
  });
  return elements;
}

function click(element, attribute, value) {
  element.listeners.click({
    target: {
      closest: (selector) => selector === `[${attribute}]`
        ? { getAttribute: () => value } : null
    }
  });
}

test('四类线面积分考点均关联题库，且可独立筛选', () => {
  const elements = start();
  const tree = elements.get('tagTree');
  for (const tag of tags) {
    assert.ok(tree.innerHTML.includes(`data-tag="${tag}"`), tag);
    const count = bank.questions.filter((q) => (q.tags || []).includes(tag)).length;
    assert.ok(count > 0, `${tag} 应有关联真题`);
    click(tree, 'data-tag', tag);
    assert.equal(elements.get('pillPool').innerHTML, `<b>${count}</b> 可抽`);
    click(tree, 'data-tag', tag);
  }
});

test('线面积分整章选择按题目去重，取消选择后恢复题库', () => {
  const elements = start();
  const count = bank.questions.filter((q) => (q.tags || []).some((tag) => tags.includes(tag))).length;
  click(elements.get('tagTree'), 'data-chapter', chapterId);
  assert.equal(elements.get('pillPool').innerHTML, `<b>${count}</b> 可抽`);
  click(elements.get('tagTree'), 'data-chapter', chapterId);
  assert.equal(elements.get('pillPool').innerHTML, `<b>${bank.questions.length}</b> 可抽`);
});

test('按线面积分整章抽题只抽中相关真题，并排除已抽记录', () => {
  const elements = start();
  const questions = bank.questions.filter((q) => (q.tags || []).some((tag) => tags.includes(tag)));
  click(elements.get('tagTree'), 'data-chapter', chapterId);
  click(elements.get('pkgChips'), 'data-pkg', 'free');
  elements.get('btnDraw').listeners.click();
  const picked = [...elements.get('previewList').innerHTML.matchAll(/data-check="([^"]+)"/g)]
    .map((match) => match[1]);
  assert.equal(picked.length, Math.min(10, questions.length));
  assert.equal(new Set(picked).size, picked.length);
  assert.ok(picked.every((id) => questions.some((q) => q.id === id)));
  assert.equal(elements.get('pillPool').innerHTML, `<b>${questions.length - picked.length}</b> 可抽`);
});

test('搜索“线面积分”可找到章节及其四类考点', () => {
  const elements = start();
  const search = elements.get('tagSearch');
  search.value = '线面积分';
  search.listeners.input();
  const tree = elements.get('tagTree').innerHTML;
  assert.ok(tree.includes(`data-chapter="${chapterId}"`));
  for (const tag of tags) assert.ok(tree.includes(`data-tag="${tag}"`), tag);
});

test('线面积分章节包含题库已有的相关考点', () => {
  const related = [...new Set(bank.questions.flatMap((q) => q.tags || []))]
    .filter((tag) => /曲[线面]积分|格林|高斯公式|斯托克斯|路径无关|积分与路径/.test(tag));
  const elements = start();
  const search = elements.get('tagSearch');
  search.value = '曲线积分与曲面积分';
  search.listeners.input();
  for (const tag of related) {
    assert.ok(elements.get('tagTree').innerHTML.includes(`data-tag="${tag}"`), tag);
  }
});
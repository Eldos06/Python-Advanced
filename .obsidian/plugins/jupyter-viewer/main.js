'use strict';

const { Plugin, FileView, MarkdownRenderer } = require('obsidian');

const VIEW_TYPE = 'jupyter-viewer';

// ── Helpers ───────────────────────────────────────────────────────────────────

function normalizeSource(source) {
    if (Array.isArray(source)) return source.join('');
    if (typeof source === 'string') return source;
    return '';
}

function stripAnsi(str) {
    return str.replace(/\x1b\[[0-9;]*[A-Za-z]/g, '');
}

// Returns { type: 'html'|'plain', content } or null
function mimeToHtml(data) {
    if (data['text/html']) {
        const raw = data['text/html'];
        return { type: 'html', content: Array.isArray(raw) ? raw.join('') : raw };
    }
    if (data['text/plain']) {
        const raw = data['text/plain'];
        return { type: 'plain', content: Array.isArray(raw) ? raw.join('') : raw };
    }
    // image/png: not present in current corpus; add here if needed:
    // if (data['image/png']) return { type: 'img', content: data['image/png'] };
    return null;
}

function renderOutput(output, container) {
    const wrap = container.createDiv({ cls: 'jv-output' });

    switch (output.output_type) {
        case 'stream': {
            const text = Array.isArray(output.text)
                ? output.text.join('')
                : (output.text || '');
            const pre = wrap.createEl('pre', { cls: 'jv-stream' });
            if (output.name === 'stderr') pre.addClass('jv-stderr');
            pre.setText(text);
            break;
        }

        case 'execute_result':
        case 'display_data': {
            const data = output.data || {};
            const result = mimeToHtml(data);
            if (!result) break;
            wrap.addClass('jv-rich-output');
            if (result.type === 'html') {
                wrap.innerHTML = result.content;
            } else {
                wrap.createEl('pre', { cls: 'jv-plain-output', text: result.content });
            }
            break;
        }

        case 'error': {
            const errorWrap = wrap.createDiv({ cls: 'jv-error' });
            const header = [output.ename, output.evalue].filter(Boolean).join(': ');
            if (header) {
                errorWrap.createEl('div', { cls: 'jv-error-header', text: header });
            }
            const tb = (output.traceback || []).map(stripAnsi).join('\n');
            if (tb) {
                errorWrap.createEl('pre', { cls: 'jv-traceback', text: tb });
            }
            break;
        }

        default:
            break;
    }
}

async function renderCell(cell, container, plugin, file) {
    const source = normalizeSource(cell.source);

    if (cell.cell_type === 'markdown') {
        if (!source.trim()) return;
        const mdWrap = container.createDiv({ cls: 'jv-cell jv-markdown-cell' });
        await MarkdownRenderer.renderMarkdown(source, mdWrap, file.path, plugin);
        return;
    }

    if (cell.cell_type === 'code') {
        const codeWrap = container.createDiv({ cls: 'jv-cell jv-code-cell' });

        const execCount = cell.execution_count;
        const badge = execCount != null ? `[${execCount}]` : '[ ]';
        codeWrap.createDiv({ cls: 'jv-exec-count', text: badge });

        const codeBlock = codeWrap.createDiv({ cls: 'jv-code-source' });
        if (source.trim()) {
            const fenced = '```python\n' + source + '\n```';
            await MarkdownRenderer.renderMarkdown(fenced, codeBlock, file.path, plugin);
        }

        const outputs = cell.outputs || [];
        if (outputs.length > 0) {
            const outputWrap = codeWrap.createDiv({ cls: 'jv-outputs' });
            for (const output of outputs) {
                renderOutput(output, outputWrap);
            }
        }
        return;
    }

    // raw cells and unknown types — skip silently
}

// ── View ──────────────────────────────────────────────────────────────────────

class JupyterView extends FileView {
    constructor(leaf, plugin) {
        super(leaf);
        this.plugin = plugin;
    }

    getViewType() {
        return VIEW_TYPE;
    }

    getDisplayText() {
        return this.file ? this.file.basename : 'Jupyter Notebook';
    }

    async onLoadFile(file) {
        const container = this.containerEl.children[1];
        container.empty();
        container.addClass('jv-container');

        try {
            const raw = await this.app.vault.read(file);
            const nb = JSON.parse(raw);
            const cells = nb.cells || [];
            for (const cell of cells) {
                await renderCell(cell, container, this.plugin, file);
            }
        } catch (err) {
            container.createEl('p', {
                cls: 'jv-parse-error',
                text: `Failed to parse notebook: ${err.message}`,
            });
        }
    }
}

// ── Plugin ────────────────────────────────────────────────────────────────────

class JupyterViewerPlugin extends Plugin {
    async onload() {
        this.registerView(VIEW_TYPE, (leaf) => new JupyterView(leaf, this));
        this.registerExtensions(['ipynb'], VIEW_TYPE);
    }

    onunload() {
        this.app.workspace.detachLeavesOfType(VIEW_TYPE);
    }
}

module.exports = JupyterViewerPlugin;

/* nosourcemap */
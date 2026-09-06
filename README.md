# Muharrir | محرر

**محرر** محرك سعودي مفتوح المصدر لتحسين الكتابة والتحرير بالعربية الفصحى المعاصرة، مع تركيز خاص على العربية المهنية في العروض الاستشارية، والتقارير، والتطبيقات، والمنصات الرقمية.

> الإصدار الحالي: `0.2.0`

## Muharrir v0.2.0

**Muharrir v0.2.0 is the first public release of Muharrir. It establishes the project's core editorial model for reviewing contemporary professional Arabic, with a focus on natural expression, meaning preservation, translation interference, terminology consistency, digital content, and consulting writing.**

- **35 core editorial rules** focused on high-value professional Arabic review.
- Three operating modes: **review**, **suggest**, and **rewrite**, with `review` as the default.
- Strong safeguards for preserving **meaning, facts, figures, names, and uncertainty**.
- Detection of **literal translation and English-shaped Arabic structures** without mechanically banning valid Arabic constructions.
- Dedicated guidance for **consulting decks and executive writing**.
- Dedicated guidance for **digital products and UI content**, including buttons, instructions, empty states, and error messages.
- **Terminology consistency** rules that distinguish official names and technical terms from ordinary prose.
- **Anti-overcorrection safeguards** so already-good Arabic is not changed merely because another wording is possible.
- Separation of **basic proofreading** from the core editorial engine through the optional `basic-proofreading` package.
- A **human-reviewed testing model**, including approved examples and `must-not-change` cases.
- Saudi-oriented source policy, prioritizing relevant authoritative Saudi Arabic and government references.
- Portable `SKILL.md` structure designed for use with **Codex and Claude-compatible skill workflows**.

## المبدأ

**محرر لا يعيد تعليم النموذج قواعد العربية الأساسية؛ بل يعالج المواضع التي لا تزال النماذج القوية تضعف فيها: أثر الترجمة، والحشو، والركاكة، والأنماط الآلية، وضعف ملاءمة السياق.**

## أوضاع التشغيل

- `review`: الوضع الافتراضي. يكشف الملاحظات ولا يعيد كتابة النص.
- `suggest`: يعرض ملاحظة ومقترحا بديلا، ولا يطبقه تلقائيا.
- `rewrite`: يعيد الصياغة عند الطلب الصريح فقط، مع المحافظة على المعنى والحقائق والنبرة.

## درجات الحكم

| الدرجة | معناها |
|---|---|
| `error` | خطأ موثق وواضح |
| `prefer` | بديل أرجح تحريريا |
| `review` | نمط يحتاج مراجعة بحسب السياق |
| `style` | سياسة أسلوب داخلية، ولا تعني خطأ البديل |
| `guardrail` | قاعدة حماية تمنع تغيير المعنى أو المعلومة |

## هيكل المشروع

```text
muharrir/
├── SKILL.md
├── README.md
├── SOURCES.md
├── DECISIONS.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── rules/
│   └── core.yml
├── optional/
│   └── basic-proofreading.yml
├── references/
│   ├── translation-and-style.md
│   ├── consulting-writing.md
│   ├── digital-content.md
│   ├── terminology.md
│   └── safety-and-overcorrection.md
├── schema/
│   └── rule.schema.json
└── tests/
    ├── reviewed-examples.yml
    ├── must-not-change.yml
    └── README.md
```

## ما الذي لا يفعله؟

- لا يهدف إلى التحايل على أدوات كشف النصوص المولدة.
- لا يدعي تحديد ما إذا كان النص قد كتبه إنسان أو نموذج.
- لا يحول كل تفضيل أسلوبي إلى خطأ لغوي.
- لا يترجم الأسماء الرسمية من عنده.
- لا يغير الحقائق أو الأرقام أو درجة اليقين لتحسين الأسلوب.
- لا يستخدم مرجعا أجنبيا للحكم على صحة العربية أو فصاحتها.

## المرجعية

المرجعية الأساسية سعودية، وتبدأ بمجمع الملك سلمان العالمي للغة العربية، ثم الأدلة والسياسات السعودية الرسمية ذات الصلة.

راجع `SOURCES.md`.

## الترخيص

MIT.

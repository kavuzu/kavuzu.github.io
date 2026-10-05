# Global Trade Atlas

**Interactive Trade & Supply Chain Intelligence · v16 Gold Master**

[Open the Atlas](https://kavuzu.github.io/) · [Deployment workflow](https://github.com/kavuzu/kavuzu.github.io/actions/workflows/deploy.yml) · [Published build metadata](https://kavuzu.github.io/version.json)

A bilingual English/Russian educational research platform connecting global geography, country evidence, products and logistics models. The complete application is the root `index.html`; it can also be downloaded and opened directly in a browser without npm, a server or a database.

## Explore

- Interactive globe and flat map; countries, ports, cities, hubs, chokepoints, corridors and product flows.
- Country intelligence, Product Deep Dive, Supply Chain Builder, bilateral and historical trade, dashboard and comparison.
- Research workspace, bookmarks, custom stories, a seven-step guided presentation, reports, PNG and print/PDF export.
- Sources & Methodology, educational compliance research, EN/RU and local preferences.

Global geographic coverage is distinct from the enhanced research-profile subset. Counts are maintained by the application registries.

## Evidence and limitations

Official observations, curated research context, representative corridors, illustrative scenarios and compliance research are different evidence types. Broad product groups use approximate HS mappings. Trade statistics do not confirm a physical shipping service, and route geography does not establish legal eligibility. Compliance research is educational, not transaction-specific legal advice.

Reporting years vary. Unavailable official observations remain unavailable rather than zero. External data refreshes require a network connection; the bundled map, research content and core workflows remain available offline. Source and research verification dates are preserved independently of deployment timestamps. The contact module prepares a draft; there is no message-sending backend.

## Publish and version

GitHub Pages serves **https://kavuzu.github.io/** using **GitHub Actions**. A push to `main` or a manual run of `Deploy Global Trade Atlas`:

1. Checks all inline JavaScript blocks and duplicate HTML IDs.
2. Copies the final Atlas into `_site/` and stamps `v16.0.N`, where `N` is this workflow's `github.run_number`.
3. Validates the artifact and deploys it to Pages.

The version appears in the title, intro, badge and centralized `ATLAS_VERSION`, including its existing report/export consumers. `_site/version.json` records the version, source commit and file hashes. Only `index.html`, `.nojekyll` and build metadata are published; project tools and README are not included in the site artifact.

Each new workflow run increments `N`; retrying the same run retains its number. Failed or cancelled runs may leave gaps among **published** versions. Keep the workflow identity to preserve its counter. A rerun for a commit that is no longer the head of `main` is rejected before deployment.

Version stamping changes the artifact only. There are **no automatic commits or tags**, no personal access token and no commit-trigger loop. The workflow has read-only repository contents access and Pages/OIDC deployment permissions. Research dates and datasets are not updated by deployment.

## Local validation

No tools are needed to open `index.html`. To reproduce the CI checks, use Node.js and Python 3:

```sh
python3 scripts/validate.py index.html
node scripts/build.mjs
python3 scripts/validate.py _site/index.html
```

A local build uses `v16.0.0`. Generated `_site/` files are ignored by Git. Edit the root source file, commit the intended changes and push to `main`; do not commit generated files.

## Русский

**Global Trade Atlas — интерактивный анализ торговли и цепочек поставок.** Это учебная исследовательская платформа с глобусом и картой, профилями стран, товарами, портами, моделями логистики, источниками и презентацией. Интерфейс доступен на русском и английском.

Официальные данные отделены от исследовательского контекста и учебных моделей. Маршрут на карте не подтверждает действующий коммерческий сервис или правомерность конкретной поставки. Отсутствующие показатели не подменяются нулями. Основные возможности и встроенные данные работают без сети; обновление внешних данных требует подключения.

Корневой `index.html` — полный финальный Atlas. Публикация запускается при push в `main`; версия `v16.0.N` присваивается опубликованному файлу по номеру запуска workflow. Автоматических коммитов нет. Старое портфолио доступно в истории Git.

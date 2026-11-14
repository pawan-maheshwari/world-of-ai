# CODEMAP (auto-generated — do not edit by hand)

Regenerate: `python3 tools/claude/codemap.py`. Line numbers are 1-based; use them with
`Read(file, offset=LINE-5, limit=80)` or `sed -n 'A,Bp' file | cut -c1-400`.
Files with *long lines* contain inline base64/minified blobs — never print those lines raw.

## File inventory (live files, largest first)

| File | Size | Lines | Long lines |
|---|---|---|---|
| `harmonia.html` | 219 KB | 2877 | 2 |
| `green-llm.html` | 157 KB | 2448 |  |
| `index.html` | 139 KB | 1245 | 3 |
| `origin-lens.html` | 85 KB | 1096 |  |
| `assay.html` | 41 KB | 472 | 1 |
| `range-studio.html` | 37 KB | 541 |  |
| `spaces/origin-lens-models/app.py` | 5 KB | 144 |  |
| `.github/workflows/deploy-origin-lens-space.yml` | 1 KB | 38 |  |

## Anchors per file

### `harmonia.html`
- L18 style
- L361 style
- L394 style
- L490 style
- L526 style
- L551 style
- L571 style
- L613 h2 `Harmon`
- L634 section `p-prompt`
- L671 section `p-atlas`
- L684 section `p-model`
- L726 section `p-ethics`
- L738 section `p-roadmap`
- L745 section `p-method`
- L833 section `p-batch`
- L851 section `p-eval`
- L887 script
- L890 data `RUBRIC_VERSION`
- L891 data `RUBRIC_DATE`
- L892 data `ENGINE_VERSION`
- L900 data `BANDS`
- L910 data `FIB`
- L911 data `BAND_CAP`
- L913 data `DIMENSIONS`
- L933 data `PROVIDERS`
- L981 data `REVIEWS`
- L1001 data `VERSIONS`
- L1010 data `PROVENANCE`
- L1028 data `ATLAS_DIMS`
- L1047 data `UPCOMING`
- L1057 data `ETH_AXES`
- L1077 data `DATA_REVIEWED`
- L1078 data `STALE_DAYS`
- L1080 data `JURIS`
- L1122 data `PLEDGES`
- L1130 data `ROADMAPS`
- L1194 data `ST_LABEL`
- L1210 data `JURIS_NAME`
- L1222 data `WPROMPT`
- L1223 data `WATL`
- L1224 data `WATL_SUM`
- L1242 data `VETO_FLOOR`
- L1249 data `CRITICAL_PROMPT`
- L1250 data `CRITICAL_ATLAS`
- L1259 data `FLOOR`
- L1276 data `NEXT_BAND`
- L1279 data `RUBRIC`
- L1392 data `INTERVALS`
- L1437 data `NOTE_INFO`
- L1569 data `PROXY_ENDPOINT`
- L1570 data `SANDBOX_ENDPOINT`
- L1571 data `JUDGE_MODEL`
- L1572 data `JUDGE_RUNS`
- L1573 data `JUDGE_TEMP`
- L1595 data `DIM_KEYS`
- L1609 data `SYS`
- L1679 data `LOCAL_RULES`
- L1768 data `LAST_READING`
- L1969 data `LC_SYS`
- L2022 data `GOLDEN`
- L2179 data `PACKS`
- L2231 data `PACK_ID`
- L2257 data `SIGN_ENDPOINT`
- L2359 data `EXTRA_RATERS`
- L2501 data `BATCH_ROWS`
- L2564 data `LIMIT`
- L2748 data `AN_SYS`
- L2826 data `COUNTER_URL`
- functions (99): daysSince@1195, staleBadge@1199, staleCount@1205, toBand@1212, bandIndex@1219, bandAt@1220, weightedMean@1225, composite@1230, atlasComposite@1231, gatedBand@1251, rubricFor@1308, biggestLever@1309, renderReport@1317, renderVersions@1341, audio@1370, intervalFor@1401, ratioFor@1405, semisForScore@1406, toVoices@1410, sound@1416, renderStaff@1446, yFor@1450, buildGauge@1511, pol@1521, arc@1522, paintGauge@1550, judgeEndpoint@1574, randomTag@1576, median@1585, validateVerdict@1596, str@1605, judgeOnce@1617, scoreViaAI@1641, scoreLocally@1694, escapeHtml@1721, optimizeLocally@1724, has@1726, renderOptimized@1747, done@1761, runId@1767, renderResult@1770, renderAtlas@1872, dots@1909, renderEthics@1910, fmtDate@1935, renderRoadmap@1937, clampScore@1968, liveCheck@1970, initLiveCheck@2009, evalRow@2071, evalMetrics@2076, unsafe@2081, flag@2082, pct@2089, renderEvalOut@2090, runEvalLocal@2137, runEvalJudge@2146, pack@2232, packW@2233, packFloor@2234, packLabel@2235, packRef@2236, canonical@2247, sha256hex@2252, sealReading@2258, b64urlEncode@2288, b64urlDecode@2291, encodeReading@2296, decodeReading@2303, permalinkFor@2314, restoreFromHash@2317, krippendorffInterval@2338, ratingSets@2360, irrReport@2367, makePerturbationProbe@2374, calibrationSVG@2395, x@2398, sparkline@2438, x@2442, historyBlock@2449, parseBatch@2475, csvCell@2486, batchCSV@2490, renderBatch@2502, batchRow@2542, runBatch@2549, worker@2566, setTab@2585, copyText@2595, ok@2596, paint@2605, renderEvalPlaceholder@2715, recentChanges@2719, checkAnnouncements@2754, wireBanner@2785, initBanner@2800, initVisitors@2827, animateCount@2843, step@2845
### `green-llm.html`
- L10 style
- L356 style
- L409 h2 `How green is`
- L436 h2 `Describe your usage`
- L516 h2 `What your usage draws`
- L527 h2 `Show the working`
- L557 h2 `What one of your prompts equals`
- L568 h2 `Five dimensions, one hundred points`
- L573 h2 `Carbon cost against value created`
- L591 h2 `The scoring matrix`
- L645 h2 `What moves the needle for you`
- L651 h2 `Which model is greenest for this workflow?`
- L733 h2 `Requirements agent`
- L811 h2 `Validation report`
- L814 h2 `Derived requirements`
- L826 h2 `Reasoning trace`
- L833 h2 `If the world worked the way you do`
- L860 h2 `In the race to adopt AI, are we missing the environment?`
- L870 h2 `How far can the environment sustain this?`
- L918 h2 `What holds the equilibrium`
- L946 h2 `Suggestions to improve the environment`
- L957 h2 `Predicted effects on the world environment`
- L1051 h2 `How the numbers are derived`
- L1129 script
- L1134 data `MODELS`
- L1141 data `GRADES`
- L1273 data `ACTIONS`
- L1443 data `TRAJ`
- L1673 data `CLASSES`
- L1680 data `CATALOG`
- L1694 data `WORKFLOWS`
- L1701 data `TIERNAME`
- L1885 data `STATE`
- L1923 data `STOP`
- L2002 h2 `Environmental position of our AI usage`
- L2007 h2 `1 · Current footprint`
- L2017 h2 `2 · Model selection for ' + w.n.toLowerCase() + '`
- L2028 h2 `3 · How long the current rate can be sustained`
- L2039 h2 `4 · Committed actions`
- L2042 h2 `5 · Agent recommendation`
- L2058 data `GRIDS`
- L2064 data `PUES`
- L2066 data `COOLS`
- L2193 data `SEV`
- functions (49): $@1154, fmt@1155, clamp@1167, readInputs@1169, physics@1186, scoreG@1200, scoreR@1209, scoreE1@1214, scoreE2@1220, scoreN@1226, grade@1230, levers@1235, delta@1237, scenarios@1264, buildActions@1324, pledge@1339, renderLedger@1356, renderFlow@1380, renderCompare@1402, renderDots@1431, renderTraj@1448, px@1451, py@1452, line@1462, renderGridFig@1497, renderRebound@1519, px@1523, py@1526, equilibrium@1548, renderAsym@1564, renderEq@1593, px@1633, py@1634, scoreModel@1704, computeModels@1717, renderModels@1740, px@1828, py@1829, kbAnswer@1922, kbPush@1946, kbAsk@1955, initKB@1962, toggle@1969, buildBoard@1978, agentValidate@2068, add@2070, agentSearch@2113, runAgent@2172, render@2297
### `index.html`
- L11 style
- L417 script
- L420 section `nav`
- L435 section `links`
- L457 section `top`
- L482 div# `panel`
- L497 section `atlas`
- L509 section `premium`
- L548 section `horizon`
- L560 section `about`
- L564 h2 `A small studio drawing a bigger map of who gets to use AI.`
- L627 section `mission`
- L635 h2 `AI for every planet.`
- L688 section `contact`
- L771 div# `modalBack`
- L779 div# `modalBody`
- L783 script
- L785 data `BEACONS`
- L878 data `THEMES`
- L1076 data `BOT_AV`
- L1081 data `BOT_INTENTS`
- L1103 data `BOT_FALLBACK`
- L1150 data `SHARE_URL`
- L1151 data `SHARE_TEXT`
- L1178 data `COUNTER`
- L1206 data `MODALS`
- functions (34): renderRows@833, selectBeacon@855, PTS@893, ll@897, rot@901, slerp@907, resize@911, hudCoord@919, draw@931, loop@1002, pos@1017, animateTo@1037, onScroll@1054, setTheme@1063, hit@1077, botReply@1104, esc@1108, botScroll@1109, addMsg@1110, clearChips@1115, addChips@1116, typing@1122, botSend@1124, openBot@1137, closeBot@1144, copyLink@1152, done@1154, fb@1155, doShare@1158, fmtCount@1179, animateCount@1180, initVisitors@1185, openModal@1237, closeModal@1238
### `origin-lens.html`
- L12 style
- L209 style
- L210 script
- L226 h2 `Origin`
- L248 section `view-text`
- L295 section `view-image`
- L345 section `view-architecture`
- L348 h2 `A pipeline modelled on SynthID Detector`
- L364 h2 `SynthID Detector and Origin Lens side by side`
- L378 section `keybox`
- L400 script
- L403 data `IN_VIEWER`
- L412 data `VIEWS`
- L457 data `LEX`
- L459 data `LEX_RE`
- L460 data `OPENER`
- L461 data `CONTR`
- L463 data `CASUAL`
- L465 data `AI_SAMPLE`
- L472 data `HU_SAMPLE`
- L553 data `TXT_SAMPLE`
- L601 data `LIBS`
- L645 data `MAX`
- L706 data `GENS`
- L820 data `GEN_SIDES`
- L829 data `SAMPLE`
- L905 data `JUDGE_PROMPT`
- L970 data `MODEL`
- L971 data `MEMKEY`
- L984 data `KEY_JUDGE`
- L1038 data `HF_SPACE`
- L1039 data `MODEL_ON`
- L1041 data `MODEL_MSG`
- functions (75): $@402, clamp@404, sig@405, css@406, escH@407, pct@408, show@413, band@420, pt@428, arc@429, gauge@430, barColor@440, renderSignals@441, setVerdict@446, toast@447, copyReport@448, reEsc@458, words@480, splitSent@481, cv@482, isHead@484, analyzeText@485, normS@528, renderText@529, runText@554, excerpt@565, runTextJudge@567, num@585, renderCuesTo@595, countWords@596, loadScript@604, cleanPdf@605, cap@607, head@608, extractText@622, openDoc@641, resetText@656, latin@672, parseExif@673, parseTiff@684, u16@686, u32@687, str@688, ifd@690, metaText@708, add@710, readMeta@739, fft@753, toGray@760, residual@761, spectrum@767, at@779, pixelAnalysis@796, drawOverlay@821, loadImg@827, analyzeImage@830, renderImage@876, runJudge@910, num@917, renderCues@927, li@928, makeSample@942, getKey@972, setKey@973, toJpegB64@974, useKey@1002, openKeybox@1012, siteSetup@1013, ap@1032, callSpace@1042, modelReset@1051, modelBusy@1052, shortName@1053, runModelText@1054, runModelImage@1069
### `assay.html`
- L12 style
- L169 h2 `Assay`
- L189 section `ledger`
- L192 h2 `The public ledger`
- L200 section `scale`
- L203 h2 `How a hallmark is struck`
- L224 section `watch`
- L227 h2 `The release watch`
- L246 script
- L248 data `ASSAY`
- L255 data `SNAPSHOT`
- L258 data `METRICS`
- L263 data `VERDICTS`
- L269 data `DIR_WORDS`
- L330 data `DATA`
- functions (20): delta@271, refVerdict@277, esc@294, phrase@295, fmtDate@301, stamp@303, bar@314, x@318, anchor@319, scoredClaims@332, renderTally@337, renderLedger@348, src@355, renderWatch@383, renderAll@394, getJSON@397, loadLive@398, setSource@406, sim@422, apply@438
### `range-studio.html`
- L16 script
- L17 style
- L276 section `agents`
- L302 section `governance`
- L306 h2 `You decide how much the agents may do on their own.`
- L330 section `evidence`
- L334 h2 `Back-test before you trust it.`
- L371 section `connectors`
- L375 h2 `Reads your extracts. Writes your load files.`
- L388 section `editions`
- L392 h2 `Start on one laptop. Grow to the whole planning team.`
- L422 section `pilot`
- L426 h2 `Evidence on your data before a live season.`
- L440 h2 `Plan by`
- L452 script
- L454 data `CONTACT`
- L466 data `AGENTS`
- L475 data `SUP`
- L507 data `ITEMS`
- L514 data `MODES`
- functions (3): mail@455, show@479, setMode@519
### `spaces/origin-lens-models/app.py`
- L80 class `TextIn`
- L85 class `ImageIn`
- functions (7): ai_probability@49, as_lists@66, chunks@71, home@95, health@110, score_text@115, score_image@134

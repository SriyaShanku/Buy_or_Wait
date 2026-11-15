# Sample mismatch audit

Generated deterministically from the current engine and supplied labels. Event lists are limited to a 120-day evidence window.

## request_01 — other (explanation only)
- First difference: `decision_explanation`; all: decision_explanation.
- Expected: `25256 | affordable_now | full_payment | 2024-03-03:25256 | 2024-03-03 | none`.
- Current: `25256 | affordable_now | full_payment | 2024-03-03:25256 | 2024-03-03 | none`.
- Profile: start `58481.1` ZAR; minimum `18000`; methods `full_payment`; deadline `2024-03-20`.
- Income evidence: event_25 salary/credit 12826 settled 2024-02-15; event_99 shopping/credit 583 settled 2024-01-29; event_103 salary/credit 23320 scheduled 2024-03-15.
- Expense evidence: event_94 dining/debit 1017.11 settled 2024-01-14; event_95 dining/debit 1222.49 settled 2024-01-28; event_96 dining/debit 1016.12 settled 2024-02-11; event_97 dining/debit 1216.17 settled 2024-02-25; event_98 shopping/debit 583 settled 2024-01-26; event_100 shopping/debit 816.2 cancelled 2024-02-16; event_101 shopping/debit 816.2 settled 2024-02-17; event_102 transport/debit 567.6 pending 2024-03-05.
- Recurrence candidates: debt_repayment: event_16,event_22,event_29; delivery_membership: event_18,event_24,event_31; dining: event_95,event_96,event_97; education: event_15,event_21,event_28; groceries: event_56,event_57,event_58; music_subscription: event_17,event_23,event_30; rent: event_19,event_26,event_32; salary: event_25,event_103; shopping: event_98,event_100,event_101; transport: event_83,event_84,event_102; utilities: event_14,event_20,event_27.
- Pending/scheduled: event_102 transport/debit 567.6 pending 2024-03-05; event_103 salary/credit 23320 scheduled 2024-03-15.
- Messages: none.
- Image evidence: none.
- Options: payment_option_01 full_payment 25256x1 from 2024-03-03 total 25256; payment_option_02 installments 1852.11x15 from 2024-03-06 total 27781.65; payment_option_03 installments 4546.08x6 from 2024-03-10 total 27276.48; payment_option_04 installments 1283.85x24 from 2024-03-17 total 30812.4.

## request_02 — 90-day forecast / earliest-full-payment calculation
- First difference: `amount_safe_to_pay`; all: amount_safe_to_pay, earliest_date_for_full_payment, decision_explanation.
- Expected: `17229139.2 | affordable_with_plan | installments | 2025-08-08:15952906.67|2025-09-07:15952906.67|2025-10-07:15952906.67 | 2025-09-15 | none`.
- Current: `29574389.21 | affordable_with_plan | installments | 2025-08-08:15952906.67|2025-09-07:15952906.67|2025-10-07:15952906.67 | 2025-08-14 | none`.
- Profile: start `60383889.2` IDR; minimum `29158400`; methods `partial_payment|installments`; deadline `2025-10-10`.
- Income evidence: event_112 salary/credit 33345000 settled 2025-04-15; event_120 salary/credit 33345000 settled 2025-05-15; event_128 salary/credit 33345000 settled 2025-06-15; event_136 salary/credit 33345000 settled 2025-07-15.
- Expense evidence: event_175 transport/debit 1062310.27 settled 2025-07-29; event_179 dining/debit 1271076.93 settled 2025-04-16; event_180 dining/debit 971169.92 settled 2025-05-07; event_181 dining/debit 1111388.15 settled 2025-05-28; event_182 dining/debit 947892.35 settled 2025-06-18; event_183 dining/debit 1043758.65 settled 2025-07-09; event_184 dining/debit 1204805.34 settled 2025-07-30; event_185 shopping/debit 1651100 pending 2025-08-08.
- Recurrence candidates: cloud_storage: event_127,event_135,event_143; dining: event_182,event_183,event_184; education: event_124,event_132,event_140; entertainment: event_126,event_134,event_142; groceries: event_160,event_161,event_162; healthcare: event_125,event_133,event_141; housing: event_129,event_137,event_144; insurance: event_123,event_131,event_139; salary: event_120,event_128,event_136; transport: event_173,event_174,event_175; utilities: event_122,event_130,event_138.
- Pending/scheduled: event_185 shopping/debit 1651100 pending 2025-08-08.
- Messages: none.
- Image evidence: none.
- Options: payment_option_05 installments 15952906.67x3 from 2025-08-08 total 47858720.01; payment_option_06 full_payment 46018000x1 from 2025-08-05 total 46018000; payment_option_07 installments 2914473.33x18 from 2025-08-12 total 52460519.94.

## request_03 — 90-day forecast / earliest-full-payment calculation
- First difference: `amount_safe_to_pay`; all: amount_safe_to_pay, payment_plan, earliest_date_for_full_payment, decision_explanation.
- Expected: `873000 | affordable_later | wait | 2019-11-15:5491000 | 2019-11-15 | none`.
- Current: `1906600.01 | affordable_later | wait | 2019-10-14:5491000 | 2019-10-14 | none`.
- Profile: start `5810300` IDR; minimum `2668700`; methods `full_payment|partial_payment|installments`; deadline `2019-11-15`.
- Income evidence: event_204 salary/credit 4365000 settled 2019-07-15; event_210 salary/credit 4365000 settled 2019-08-15; event_211 salary/credit 1964250 settled 2019-08-20; event_253 salary/credit 4365000 settled 2019-08-31.
- Expense evidence: event_243 transport/debit 106233.46 settled 2019-08-28; event_247 dining/debit 132247.64 settled 2019-05-11; event_248 dining/debit 158476.5 settled 2019-06-01; event_249 dining/debit 175170.67 settled 2019-06-22; event_250 dining/debit 171303.21 settled 2019-07-13; event_251 dining/debit 171191.99 settled 2019-08-03; event_252 dining/debit 135718.35 settled 2019-08-24; event_254 healthcare/debit 95000 pending 2019-09-07.
- Recurrence candidates: cloud_storage: event_201,event_207,event_214; dining: event_250,event_251,event_252; groceries: event_232,event_233,event_234; rent: event_199,event_205,event_212; salary: event_210,event_211,event_253; shopping: event_203,event_209,event_216; streaming: event_202,event_208,event_215; transport: event_241,event_242,event_243; utilities: event_200,event_206,event_213.
- Pending/scheduled: event_254 healthcare/debit 95000 pending 2019-09-07.
- Messages: Tim payroll BrightPath Media telah mengirim pembaruan. Gaji rutin untuk penggajian berikutnya sudah dikonfirmasi. Slip gaji berikutnya akan .
- Image evidence: image_01 -> Extraction(amount=Decimal('4365000'), confidence='reviewed', source='reviewed_receipt', note='reviewed visible receipt total').
- Options: payment_option_08 full_payment 5491000x1 from 2019-09-03 total 5491000; payment_option_09 installments 308541.9x21 from 2019-09-17 total 6479379.9; payment_option_10 installments 279125.83x24 from 2019-09-06 total 6699019.92.

## request_04 — recurrence handling / 90-day forecast
- First difference: `amount_safe_to_pay`; all: amount_safe_to_pay, affordability_status, recommended_payment_method, payment_plan, earliest_date_for_full_payment, decision_explanation.
- Expected: `8401800 | affordable_later | wait | 2024-06-15:12693000 | 2024-06-15 | none`.
- Current: `2637792.87 | not_affordable | not_recommended | none |  | none`.
- Profile: start `52206950` IDR; minimum `30686600`; methods `full_payment`; deadline `2024-06-19`.
- Income evidence: event_269 salary/credit 38190000 settled 2024-03-15; event_270 salary/credit 10498464.28 settled 2024-03-22; event_277 salary/credit 38190000 settled 2024-04-15; event_284 salary/credit 38190000 settled 2024-05-15.
- Expense evidence: event_350 dining/debit 1551598.07 settled 2024-03-04; event_351 dining/debit 2102251.18 settled 2024-03-18; event_352 dining/debit 1282286.6 settled 2024-04-01; event_353 dining/debit 1259307.64 settled 2024-04-15; event_354 dining/debit 1661337.11 settled 2024-04-29; event_355 dining/debit 1886856.1 settled 2024-05-13; event_356 dining/debit 2108488.15 settled 2024-05-27; event_357 education/debit 1704300 scheduled 2024-06-11.
- Recurrence candidates: delivery_membership: event_274,event_281,event_288; dining: event_354,event_355,event_356; entertainment: event_276,event_283,event_290; groceries: event_315,event_316,event_317; gym: event_275,event_282,event_289; music_subscription: event_273,event_280,event_287; rent: event_278,event_285,event_291; salary: event_270,event_277,event_284; transport: event_341,event_342,event_343; utilities: event_272,event_279,event_286.
- Pending/scheduled: event_357 education/debit 1704300 scheduled 2024-06-11.
- Messages: Rincian penggajian Anda di Greenfield Foods telah berubah. Bonus kuartalan Anda masih menunggu hasil akhir penilaian kinerja. Jumlah akhir d.
- Image evidence: none.
- Options: payment_option_11 full_payment 12693000x1 from 2024-06-04 total 12693000; payment_option_12 installments 875817x15 from 2024-06-04 total 13137255.

## request_05 — recurrence handling / 90-day forecast
- First difference: `amount_safe_to_pay`; all: amount_safe_to_pay, affordability_status, recommended_payment_method, payment_plan, earliest_date_for_full_payment, decision_explanation.
- Expected: `737 | not_affordable | not_recommended | none |  | none`.
- Current: `15488 | affordable_now | full_payment | 2025-11-06:15488 | 2025-11-06 | none`.
- Profile: start `46475.1` ZAR; minimum `13100`; methods `full_payment|partial_payment|installments`; deadline `2026-01-12`.
- Income evidence: event_366 salary/credit 14740 settled 2025-07-15; event_374 salary/credit 14740 settled 2025-08-15; event_382 salary/credit 14740 settled 2025-09-15; event_390 salary/credit 14740 settled 2025-10-15.
- Expense evidence: event_431 transport/debit 431.81 settled 2025-08-06; event_432 transport/debit 354.2 settled 2025-08-20; event_433 transport/debit 485.59 settled 2025-09-03; event_434 transport/debit 411.47 settled 2025-09-17; event_435 transport/debit 377.26 settled 2025-10-01; event_436 transport/debit 352.46 settled 2025-10-15; event_437 transport/debit 388.74 settled 2025-10-29; event_438 utilities/debit 389.4 failed 2025-11-04.
- Recurrence candidates: cloud_storage: event_380,event_388,event_396; debt_repayment: event_377,event_385,event_393; family_support: event_379,event_387,event_395; groceries: event_422,event_423,event_424; healthcare: event_378,event_386,event_394; rent: event_383,event_391,event_398; salary: event_374,event_382,event_390; shopping: event_381,event_389,event_397; transport: event_435,event_436,event_437; utilities: event_384,event_392,event_438.
- Pending/scheduled: none.
- Messages: none.
- Image evidence: none.
- Options: payment_option_13 full_payment 15488x1 from 2025-11-06 total 15488; payment_option_14 installments 980.91x18 from 2025-11-09 total 17656.38; payment_option_15 installments 787.31x24 from 2025-11-20 total 18895.44.

## request_06 — recurrence handling / spending-change logic
- First difference: `amount_safe_to_pay`; all: amount_safe_to_pay, affordability_status, payment_plan, earliest_date_for_full_payment, spending_changes_needed, decision_explanation.
- Expected: `603.3 | affordable_with_plan | full_payment | 2026-01-03:620.40 | 2026-01-15 | stop:event_476`.
- Current: `620.4 | affordable_now | full_payment | 2026-01-03:620.4 | 2026-01-03 | none`.
- Profile: start `1942.4` EUR; minimum `800`; methods `full_payment|partial_payment`; deadline `2026-01-14`.
- Income evidence: event_447 salary/credit 1441 settled 2025-09-15; event_455 salary/credit 1441 settled 2025-10-15; event_463 salary/credit 1037.52 settled 2025-11-15; event_471 salary/credit 1037.52 settled 2025-12-15.
- Expense evidence: event_550 dining/debit 37.42 settled 2025-11-16; event_551 dining/debit 55.16 settled 2025-11-23; event_552 dining/debit 57.57 settled 2025-11-30; event_553 dining/debit 45.39 settled 2025-12-07; event_554 dining/debit 36 settled 2025-12-14; event_555 dining/debit 57.28 settled 2025-12-21; event_556 dining/debit 48.36 settled 2025-12-28; event_557 shopping/debit 66 cancelled 2025-12-31.
- Recurrence candidates: cloud_storage: event_459,event_467,event_475; dining: event_554,event_555,event_556; entertainment: event_462,event_470,event_478; groceries: event_494,event_495,event_496; insurance: event_458,event_466,event_474; rent: event_456,event_464,event_472; salary: event_455,event_463,event_471; shopping: event_469,event_477,event_557; streaming: event_460,event_468,event_476; transport: event_529,event_530,event_531; utilities: event_457,event_465,event_473.
- Pending/scheduled: none.
- Messages: Here’s the latest payroll information from Northstar Labs. Your temporary monthly pay is EUR 1037.52. The reduced amount continues for the n.
- Image evidence: none.
- Options: payment_option_16 full_payment 620.4x1 from 2026-01-03 total 620.4; payment_option_17 installments 34.86x21 from 2026-01-10 total 732.06; payment_option_18 installments 111.67x6 from 2026-01-17 total 670.02.

## request_07 — 90-day forecast / earliest-full-payment calculation
- First difference: `amount_safe_to_pay`; all: amount_safe_to_pay, earliest_date_for_full_payment, decision_explanation.
- Expected: `87170.56 | affordable_with_plan | installments | 2024-09-12:68432|2024-10-10:68432|2024-11-07:68432 | 2024-10-23 | none`.
- Current: `104086 | affordable_with_plan | installments | 2024-09-12:68432|2024-10-10:68432|2024-11-07:68432 | 2024-09-22 | none`.
- Profile: start `218945.56` INR; minimum `93000`; methods `installments`; deadline `2024-11-14`.
- Income evidence: event_563 salary/credit 149000 settled 2024-05-15; event_568 salary/credit 149000 settled 2024-06-15; event_573 salary/credit 149000 settled 2024-07-15; event_578 salary/credit 149000 settled 2024-08-23.
- Expense evidence: event_604 transport/debit 3773.92 settled 2024-08-09; event_605 transport/debit 3145.62 settled 2024-08-30; event_609 dining/debit 6313.91 settled 2024-05-13; event_610 dining/debit 5802.49 settled 2024-06-03; event_611 dining/debit 4541.62 settled 2024-06-24; event_612 dining/debit 6664.9 settled 2024-07-15; event_613 dining/debit 5799.66 settled 2024-08-05; event_614 dining/debit 6493.86 settled 2024-08-26.
- Recurrence candidates: debt_repayment: event_571,event_576,event_581; dining: event_612,event_613,event_614; groceries: event_594,event_595,event_596; music_subscription: event_572,event_577,event_582; rent: event_574,event_579,event_583; salary: event_568,event_573,event_578; transport: event_603,event_604,event_605; utilities: event_570,event_575,event_580.
- Pending/scheduled: none.
- Messages: none.
- Image evidence: none.
- Options: payment_option_19 installments 68432x3 from 2024-09-12 total 205296; payment_option_20 full_payment 197400x1 from 2024-09-05 total 197400; payment_option_21 installments 14476x15 from 2024-09-19 total 217140.

## request_08 — 90-day forecast / earliest-full-payment calculation
- First difference: `amount_safe_to_pay`; all: amount_safe_to_pay, payment_plan, earliest_date_for_full_payment, decision_explanation.
- Expected: `284.57 | affordable_later | wait | 2025-04-15:996.60 | 2025-04-15 | none`.
- Current: `736.58 | affordable_later | wait | 2025-02-14:996.6 | 2025-02-14 | none`.
- Profile: start `1536.57` EUR; minimum `800`; methods `full_payment`; deadline `2025-04-15`.
- Income evidence: event_622 salary/credit 1422.85 settled 2024-10-15; event_629 salary/credit 1422.85 settled 2024-11-15; event_636 salary/credit 1422.85 settled 2024-12-15; event_643 salary/credit 782.57 settled 2025-01-15.
- Expense evidence: event_709 dining/debit 41.5 settled 2024-10-24; event_710 dining/debit 58.15 settled 2024-11-07; event_711 dining/debit 45.5 settled 2024-11-21; event_712 dining/debit 46.75 settled 2024-12-05; event_713 dining/debit 49.45 settled 2024-12-19; event_714 dining/debit 56.05 settled 2025-01-02; event_715 dining/debit 53.65 settled 2025-01-16; event_716 dining/debit 42.33 settled 2025-01-30.
- Recurrence candidates: debt_repayment: event_633,event_640,event_647; delivery_membership: event_635,event_642,event_649; dining: event_714,event_715,event_716; education: event_632,event_639,event_646; groceries: event_675,event_676,event_677; music_subscription: event_634,event_641,event_648; rent: event_637,event_644,event_650; salary: event_629,event_636,event_643; transport: event_701,event_702,event_703; utilities: event_638,event_645,event_651.
- Pending/scheduled: none.
- Messages: Hi, Greenfield Foods payroll here. Your next salary is reduced to EUR 1422.85. The adjustment is due to approved unpaid leave. The adjustmen.
- Image evidence: none.
- Options: payment_option_22 full_payment 996.6x1 from 2025-02-07 total 996.6; payment_option_23 installments 63.12x18 from 2025-02-07 total 1136.16.

## request_09 — other (explanation only)
- First difference: `decision_explanation`; all: decision_explanation.
- Expected: `166.61 | affordable_now | full_payment | 2026-07-04:166.61 | 2026-07-04 | none`.
- Current: `166.61 | affordable_now | full_payment | 2026-07-04:166.61 | 2026-07-04 | none`.
- Profile: start `2231.1` EUR; minimum `600`; methods `full_payment|partial_payment|installments`; deadline `2026-07-23`.
- Income evidence: event_738 salary/credit 506.35 settled 2026-05-07; event_739 salary/credit 441.96 settled 2026-05-20; event_745 salary/credit 547.55 settled 2026-06-07; event_746 salary/credit 361.45 settled 2026-06-20.
- Expense evidence: event_778 transport/debit 27.2 settled 2026-06-05; event_779 transport/debit 24.13 settled 2026-06-26; event_783 dining/debit 31.15 settled 2026-03-14; event_784 dining/debit 23.42 settled 2026-04-04; event_785 dining/debit 28.41 settled 2026-04-25; event_786 dining/debit 35.49 settled 2026-05-16; event_787 dining/debit 27.38 settled 2026-06-06; event_788 dining/debit 29.16 settled 2026-06-27.
- Recurrence candidates: cloud_storage: event_735,event_742,event_749; dining: event_786,event_787,event_788; groceries: event_768,event_769,event_770; rent: event_740,event_747,event_752; salary: event_739,event_745,event_746; shopping: event_737,event_744,event_751; streaming: event_736,event_743,event_750; transport: event_777,event_778,event_779; utilities: event_734,event_741,event_748.
- Pending/scheduled: none.
- Messages: none.
- Image evidence: none.
- Options: payment_option_24 full_payment 166.61x1 from 2026-07-04 total 166.61; payment_option_25 installments 8.22x21 from 2026-07-07 total 172.62; payment_option_26 installments 7.29x24 from 2026-07-18 total 174.96.

## request_10 — 90-day forecast
- First difference: `amount_safe_to_pay`; all: amount_safe_to_pay, decision_explanation.
- Expected: `12700 | not_affordable | not_recommended | none |  | none`.
- Current: `266700 | not_affordable | not_recommended | none |  | none`.
- Profile: start `750155` INR; minimum `225400`; methods `partial_payment|installments`; deadline `2025-02-10`.
- Income evidence: event_830 salary/credit 44415.5 settled 2024-11-11; event_831 salary/credit 47802.51 settled 2024-11-18; event_832 salary/credit 82667.27 settled 2024-11-25; event_839 salary/credit 52239.8 settled 2024-12-04.
- Expense evidence: event_897 dining/debit 9621.2 settled 2024-08-24; event_898 dining/debit 6375.03 settled 2024-09-07; event_899 dining/debit 10079.99 settled 2024-09-21; event_900 dining/debit 10525.43 settled 2024-10-05; event_901 dining/debit 8538.83 settled 2024-10-19; event_902 dining/debit 8480.31 settled 2024-11-02; event_903 dining/debit 8253.71 settled 2024-11-16; event_904 dining/debit 10370.83 settled 2024-11-30.
- Recurrence candidates: delivery_membership: event_816,event_826,event_836; dining: event_902,event_903,event_904; entertainment: event_818,event_828,event_838; groceries: event_864,event_865,event_866; gym: event_817,event_827,event_837; music_subscription: event_815,event_825,event_835; rent: event_823,event_833,event_840; salary: event_831,event_832,event_839; transport: event_889,event_890,event_891; utilities: event_814,event_824,event_834.
- Pending/scheduled: none.
- Messages: Here’s the latest service update from QuickCrew. The next QuickCrew payout is still pending. The weekly earnings shown in the QuickCrew app .
- Image evidence: none.
- Options: payment_option_27 full_payment 266700x1 from 2024-12-06 total 266700; payment_option_28 installments 19558x15 from 2024-12-13 total 293370.

## request_11 — recurrence handling / spending-change logic
- First difference: `amount_safe_to_pay`; all: amount_safe_to_pay, affordability_status, earliest_date_for_full_payment, spending_changes_needed, decision_explanation.
- Expected: `12510645 | affordable_with_plan | full_payment | 2025-05-03:13110000 | 2025-07-15 | reduce_to:event_989:665950`.
- Current: `13110000 | affordable_now | full_payment | 2025-05-03:13110000 | 2025-05-03 | none`.
- Profile: start `63531795` IDR; minimum `34140600`; methods `full_payment`; deadline `2025-06-12`.
- Income evidence: event_932 salary/credit 23256000 settled 2025-03-15; event_933 salary/credit 20012106.46 settled 2025-03-24; event_941 salary/credit 23256000 settled 2025-04-15; event_942 salary/credit 8502888.2 settled 2025-04-24.
- Expense evidence: event_979 transport/debit 1103949.29 settled 2025-04-13; event_980 transport/debit 1244835.69 settled 2025-04-27; event_984 dining/debit 1697463.1 settled 2025-01-08; event_985 dining/debit 1052748.56 settled 2025-01-29; event_986 dining/debit 1365643.7 settled 2025-02-19; event_987 dining/debit 1335266.7 settled 2025-03-12; event_988 dining/debit 1503635.49 settled 2025-04-02; event_989 dining/debit 1163530.49 settled 2025-04-23.
- Recurrence candidates: cloud_storage: event_931,event_940,event_949; dining: event_987,event_988,event_989; education: event_928,event_937,event_946; entertainment: event_930,event_939,event_948; groceries: event_965,event_966,event_967; healthcare: event_929,event_938,event_947; housing: event_925,event_934,event_943; insurance: event_927,event_936,event_945; salary: event_933,event_941,event_942; transport: event_978,event_979,event_980; utilities: event_926,event_935,event_944.
- Pending/scheduled: none.
- Messages: Berikut informasi penggajian terbaru dari Greenfield Foods. Gaji pokok yang dikonfirmasi adalah IDR 38760000. Komisi dari transaksi yang mas.
- Image evidence: none.
- Options: payment_option_29 full_payment 13110000x1 from 2025-05-03 total 13110000; payment_option_30 installments 830300x18 from 2025-05-17 total 14945400; payment_option_31 installments 2359800x6 from 2025-05-03 total 14158800; payment_option_32 installments 666425x24 from 2025-05-06 total 15994200.

## request_12 — other (explanation only)
- First difference: `decision_explanation`; all: decision_explanation.
- Expected: `65164 | affordable_with_plan | installments | 2026-04-19:22590.19|2026-05-20:22590.19|2026-06-20:22590.19 | 2026-04-05 | none`.
- Current: `65164 | affordable_with_plan | installments | 2026-04-19:22590.19|2026-05-20:22590.19|2026-06-20:22590.19 | 2026-04-05 | none`.
- Profile: start `193089.89` ZAR; minimum `43200`; methods `partial_payment|installments`; deadline `2026-06-20`.
- Income evidence: event_996 salary/credit 41904.42 settled 2025-12-15; event_1002 salary/credit 61315.12 settled 2026-01-15.
- Expense evidence: event_1044 transport/debit 1684.28 settled 2026-03-06; event_1045 transport/debit 1679.15 settled 2026-03-27; event_1049 dining/debit 2554.33 settled 2025-12-13; event_1050 dining/debit 2344.45 settled 2026-01-03; event_1051 dining/debit 2608.96 settled 2026-01-24; event_1052 dining/debit 1765.33 settled 2026-02-14; event_1053 dining/debit 2089.92 settled 2026-03-07; event_1054 dining/debit 1943.35 settled 2026-03-28.
- Recurrence candidates: cloud_storage: event_1005,event_1010,event_1015; dining: event_1052,event_1053,event_1054; groceries: event_1034,event_1035,event_1036; rent: event_1008,event_1013,event_1018; salary: event_996,event_1002; shopping: event_1007,event_1012,event_1017; streaming: event_1006,event_1011,event_1016; transport: event_1043,event_1044,event_1045; utilities: event_1004,event_1009,event_1014.
- Pending/scheduled: none.
- Messages: none.
- Image evidence: none.
- Options: payment_option_33 installments 22590.19x3 from 2026-04-19 total 67770.57; payment_option_34 full_payment 65164x1 from 2026-04-05 total 65164; payment_option_35 installments 3661.6x21 from 2026-04-05 total 76893.6.

## request_13 — 90-day forecast / earliest-full-payment calculation
- First difference: `amount_safe_to_pay`; all: amount_safe_to_pay, affordability_status, recommended_payment_method, payment_plan, earliest_date_for_full_payment, decision_explanation.
- Expected: `433.4 | affordable_later | wait | 2024-05-15:941.60 | 2024-05-15 | none`.
- Current: `941.6 | affordable_now | full_payment | 2024-03-07:941.6 | 2024-03-07 | none`.
- Profile: start `2789.52` EUR; minimum `1300`; methods `full_payment`; deadline `2024-05-15`.
- Income evidence: event_1079 salary/credit 1343.54 settled 2024-01-15; event_1080 salary/credit 881.45 settled 2024-01-20; event_1087 salary/credit 1343.54 settled 2024-02-15; event_1161 salary/credit 1343.54 scheduled 2024-03-15.
- Expense evidence: event_1153 dining/debit 80.35 settled 2023-11-23; event_1154 dining/debit 64.45 settled 2023-12-07; event_1155 dining/debit 70.45 settled 2023-12-21; event_1156 dining/debit 61.59 settled 2024-01-04; event_1157 dining/debit 48.2 settled 2024-01-18; event_1158 dining/debit 60.34 settled 2024-02-01; event_1159 dining/debit 48.02 settled 2024-02-15; event_1160 dining/debit 61.28 settled 2024-02-29.
- Recurrence candidates: delivery_membership: event_1076,event_1084,event_1091; dining: event_1158,event_1159,event_1160; entertainment: event_1078,event_1086,event_1093; groceries: event_1119,event_1120,event_1121; gym: event_1077,event_1085,event_1092; music_subscription: event_1075,event_1083,event_1090; rent: event_1081,event_1088,event_1094; salary: event_1080,event_1087,event_1161; transport: event_1145,event_1146,event_1147; utilities: event_1082,event_1089,event_1095.
- Pending/scheduled: event_1161 salary/credit 1343.54 scheduled 2024-03-15.
- Messages: none.
- Image evidence: none.
- Options: payment_option_36 full_payment 941.6x1 from 2024-03-07 total 941.6; payment_option_37 installments 69.05x15 from 2024-03-10 total 1035.75; payment_option_38 installments 47.86x24 from 2024-03-21 total 1148.64.

## request_14 — 90-day forecast
- First difference: `amount_safe_to_pay`; all: amount_safe_to_pay, decision_explanation.
- Expected: `597.74 | not_affordable | not_recommended | none |  | none`.
- Current: `1235.34 | not_affordable | not_recommended | none |  | none`.
- Profile: start `3931.74` EUR; minimum `2200`; methods `partial_payment`; deadline `2025-10-04`.
- Income evidence: event_1170 salary/credit 2717 settled 2025-04-15; event_1192 salary/credit 2717 settled 2025-07-15.
- Expense evidence: event_1232 transport/debit 56.49 settled 2025-04-21; event_1233 transport/debit 55.52 settled 2025-05-05; event_1234 transport/debit 52.26 settled 2025-05-19; event_1235 transport/debit 50.48 settled 2025-06-02; event_1236 transport/debit 55.96 settled 2025-06-16; event_1237 transport/debit 62.3 settled 2025-06-30; event_1238 transport/debit 43.12 settled 2025-07-14; event_1239 transport/debit 43.88 settled 2025-07-28.
- Recurrence candidates: cloud_storage: event_1183,event_1190,event_1198; debt_repayment: event_1180,event_1187,event_1195; family_support: event_1182,event_1189,event_1197; groceries: event_1224,event_1225,event_1226; healthcare: event_1181,event_1188,event_1196; rent: event_1185,event_1193,event_1200; salary: event_1170,event_1192; shopping: event_1184,event_1191,event_1199; transport: event_1237,event_1238,event_1239; utilities: event_1179,event_1186,event_1194.
- Pending/scheduled: none.
- Messages: none.
- Image evidence: none.
- Options: payment_option_39 full_payment 5414.2x1 from 2025-08-04 total 5414.2; payment_option_40 installments 342.9x18 from 2025-08-11 total 6172.2.

## request_15 — 90-day forecast
- First difference: `amount_safe_to_pay`; all: amount_safe_to_pay, decision_explanation.
- Expected: `83.05 | not_affordable | not_recommended | none |  | none`.
- Current: `0 | not_affordable | not_recommended | none |  | none`.
- Profile: start `1770.05` EUR; minimum `1200`; methods `partial_payment`; deadline `2026-02-01`.
- Income evidence: event_1258 salary/credit 1661 settled 2025-11-15; event_1265 salary/credit 1661 settled 2025-12-15.
- Expense evidence: event_1328 dining/debit 36.23 settled 2025-09-20; event_1329 dining/debit 32.17 settled 2025-10-04; event_1330 dining/debit 34.51 settled 2025-10-18; event_1331 dining/debit 38.56 settled 2025-11-01; event_1332 dining/debit 51.08 settled 2025-11-15; event_1333 dining/debit 32.62 settled 2025-11-29; event_1334 dining/debit 38.07 settled 2025-12-13; event_1335 dining/debit 49.35 settled 2025-12-27.
- Recurrence candidates: debt_repayment: event_1255,event_1262,event_1269; delivery_membership: event_1257,event_1264,event_1271; dining: event_1333,event_1334,event_1335; education: event_1254,event_1261,event_1268; groceries: event_1295,event_1296,event_1297; music_subscription: event_1256,event_1263,event_1270; rent: event_1259,event_1266,event_1272; salary: event_1258,event_1265; transport: event_1320,event_1321,event_1322; utilities: event_1253,event_1260,event_1267.
- Pending/scheduled: none.
- Messages: A quick update from the payroll team at Riverline Retail. Your first salary will be EUR 1661. The confirmed credit date is 2026-01-15. The m.
- Image evidence: none.
- Options: payment_option_41 full_payment 3685x1 from 2026-01-06 total 3685; payment_option_42 installments 207.06x21 from 2026-01-20 total 4348.26; payment_option_43 installments 187.32x24 from 2026-01-09 total 4495.68.

## request_16 — image amount interpretation / event status-lifecycle handling
- First difference: `amount_safe_to_pay`; all: amount_safe_to_pay, affordability_status, recommended_payment_method, payment_plan, earliest_date_for_full_payment, decision_explanation.
- Expected: `122500 | affordable_now | full_payment | 2023-08-12:122500 | 2023-08-12 | none`.
- Current: `55107.09 | affordable_later | wait | 2023-09-13:122500 | 2023-09-13 | none`.
- Profile: start `362370` INR; minimum `122400`; methods `full_payment|installments`; deadline `2023-10-11`.
- Income evidence: event_1343 salary/credit 173000 settled 2023-04-15; event_1350 salary/credit 173000 settled 2023-05-15; event_1357 salary/credit 173000 settled 2023-06-15; event_1364 salary/credit 173000 settled 2023-07-15.
- Expense evidence: event_1435 dining/debit 3794.56 settled 2023-05-12; event_1436 dining/debit 5905.06 settled 2023-05-26; event_1437 dining/debit 5981.93 settled 2023-06-09; event_1438 dining/debit 5210.3 settled 2023-06-23; event_1439 dining/debit 3835.73 settled 2023-07-07; event_1440 dining/debit 6354.26 settled 2023-07-21; event_1441 dining/debit 5256.32 settled 2023-08-04; event_1442 rent/debit 100000 scheduled 2023-08-16.
- Recurrence candidates: cloud_storage: event_1362,event_1369,event_1375; debt_repayment: event_1360,event_1367,event_1373; dining: event_1439,event_1440,event_1441; groceries: event_1400,event_1401,event_1402; rent: event_1365,event_1371,event_1442; salary: event_1350,event_1357,event_1364; shopping: event_1363,event_1370,event_1376; streaming: event_1361,event_1368,event_1374; transport: event_1426,event_1427,event_1428; utilities: event_1359,event_1366,event_1372.
- Pending/scheduled: event_1442 rent/debit 100000 scheduled 2023-08-16.
- Messages: StayLedger wanted to let you know about a change on your account. The renewed lease increases monthly rent by 12%. The new amount will be us.
- Image evidence: image_02 -> Extraction(amount=Decimal('100000'), confidence='reviewed', source='reviewed_receipt', note='reviewed visible receipt total').
- Options: payment_option_44 full_payment 122500x1 from 2023-08-12 total 122500; payment_option_45 installments 8983.33x15 from 2023-08-12 total 134749.95; payment_option_46 installments 22050x6 from 2023-08-15 total 132300.

## request_17 — 90-day forecast / earliest-full-payment calculation
- First difference: `amount_safe_to_pay`; all: amount_safe_to_pay, earliest_date_for_full_payment, decision_explanation.
- Expected: `243849.58 | affordable_with_plan | installments | 2026-03-01:95194.67|2026-03-31:95194.67|2026-04-30:95194.67 | 2026-03-15 | none`.
- Current: `274600 | affordable_with_plan | installments | 2026-03-01:95194.67|2026-03-31:95194.67|2026-04-30:95194.67 | 2026-03-01 | none`.
- Profile: start `550379.58` INR; minimum `166100`; methods `installments`; deadline `2026-05-04`.
- Income evidence: event_1464 salary/credit 206000 settled 2026-01-15; event_1471 salary/credit 206000 settled 2026-02-15; event_1544 work_expense/credit 12360 settled 2026-02-26; event_1546 salary/credit 206000 scheduled 2026-03-15.
- Expense evidence: event_1537 dining/debit 6048.91 settled 2025-12-14; event_1538 dining/debit 6795.26 settled 2025-12-28; event_1539 dining/debit 6797.26 settled 2026-01-11; event_1540 dining/debit 5254.41 settled 2026-01-25; event_1541 dining/debit 6688.81 settled 2026-02-08; event_1542 dining/debit 4747.76 settled 2026-02-22; event_1543 work_expense/debit 12360 settled 2026-01-26; event_1545 groceries/debit 4122 settled 2026-02-27.
- Recurrence candidates: debt_repayment: event_1461,event_1468,event_1475; delivery_membership: event_1463,event_1470,event_1477; dining: event_1540,event_1541,event_1542; education: event_1460,event_1467,event_1474; groceries: event_1502,event_1503,event_1545; music_subscription: event_1462,event_1469,event_1476; rent: event_1458,event_1465,event_1472; salary: event_1464,event_1471,event_1546; transport: event_1527,event_1528,event_1529; utilities: event_1459,event_1466,event_1473.
- Pending/scheduled: event_1546 salary/credit 206000 scheduled 2026-03-15.
- Messages: none.
- Image evidence: image_03 -> Extraction(amount=Decimal('4122'), confidence='reviewed', source='reviewed_receipt', note='reviewed visible receipt total').
- Options: payment_option_47 installments 95194.67x3 from 2026-03-01 total 285584.01; payment_option_48 full_payment 274600x1 from 2026-03-01 total 274600; payment_option_49 installments 17391.33x18 from 2026-03-04 total 313043.94.

## request_18 — 90-day forecast / earliest-full-payment calculation
- First difference: `amount_safe_to_pay`; all: amount_safe_to_pay, payment_plan, earliest_date_for_full_payment, decision_explanation.
- Expected: `462 | affordable_later | wait | 2026-09-15:3246.10 | 2026-09-15 | none`.
- Current: `811.93 | affordable_later | wait | 2026-08-14:3246.1 | 2026-08-14 | none`.
- Profile: start `2486` EUR; minimum `1400`; methods `full_payment|partial_payment`; deadline `2026-09-15`.
- Income evidence: event_1553 salary/credit 2310 settled 2026-03-15; event_1559 salary/credit 2310 settled 2026-04-15; event_1565 salary/credit 2310 settled 2026-05-15; event_1571 salary/credit 2310 settled 2026-06-15.
- Expense evidence: event_1614 dining/debit 75.46 settled 2026-03-25; event_1615 dining/debit 66.71 settled 2026-04-08; event_1616 dining/debit 103.86 settled 2026-04-22; event_1617 dining/debit 81.05 settled 2026-05-06; event_1618 dining/debit 101.82 settled 2026-05-20; event_1619 dining/debit 62.87 settled 2026-06-03; event_1620 dining/debit 82.67 settled 2026-06-17; event_1621 dining/debit 101.88 settled 2026-07-01.
- Recurrence candidates: dining: event_1619,event_1620,event_1621; groceries: event_1593,event_1594,event_1595; healthcare: event_1563,event_1569,event_1575; housing: event_1566,event_1572,event_1577; insurance: event_1562,event_1568,event_1574; salary: event_1559,event_1565,event_1571; streaming: event_1564,event_1570,event_1576; transport: event_1606,event_1607,event_1608; utilities: event_1561,event_1567,event_1573.
- Pending/scheduled: none.
- Messages: There’s an update from Summit Bank on your recent account activity. The matching debit and credit came from a transfer between your two acco.
- Image evidence: none.
- Options: payment_option_50 full_payment 3246.1x1 from 2026-07-07 total 3246.1; payment_option_51 installments 182.4x21 from 2026-07-14 total 3830.4.

## request_19 — payment-option selection / earliest-full-payment calculation
- First difference: `amount_safe_to_pay`; all: amount_safe_to_pay, recommended_payment_method, payment_plan, earliest_date_for_full_payment, decision_explanation.
- Expected: `28820 | affordable_with_plan | partial_payment | 2024-09-04:28820|2024-09-15:10840 | 2024-09-15 | none`.
- Current: `39660 | affordable_with_plan | installments | 2024-09-04:20623.2|2024-10-02:20623.2 | 2024-09-04 | none`.
- Profile: start `199545` INR; minimum `92800`; methods `partial_payment|installments`; deadline `2024-10-04`.
- Income evidence: event_1630 salary/credit 131000 settled 2024-05-15; event_1638 salary/credit 131000 settled 2024-06-15; event_1646 salary/credit 131000 settled 2024-07-15; event_1654 salary/credit 131000 settled 2024-08-15.
- Expense evidence: event_1693 transport/debit 2610.24 settled 2024-06-06; event_1694 transport/debit 2788.22 settled 2024-06-20; event_1695 transport/debit 3242.46 settled 2024-07-04; event_1696 transport/debit 3659.94 settled 2024-07-18; event_1697 transport/debit 2759.93 settled 2024-08-01; event_1698 transport/debit 2462.29 settled 2024-08-15; event_1699 transport/debit 2765.93 settled 2024-08-29; event_1700 groceries/debit 2854 settled 2024-09-03.
- Recurrence candidates: cloud_storage: event_1644,event_1652,event_1660; debt_repayment: event_1641,event_1649,event_1657; family_support: event_1643,event_1651,event_1659; groceries: event_1685,event_1686,event_1700; healthcare: event_1642,event_1650,event_1658; rent: event_1639,event_1647,event_1655; salary: event_1638,event_1646,event_1654; shopping: event_1645,event_1653,event_1661; transport: event_1697,event_1698,event_1699; utilities: event_1640,event_1648,event_1656.
- Pending/scheduled: none.
- Messages: none.
- Image evidence: image_04 -> Extraction(amount=Decimal('2854'), confidence='reviewed', source='reviewed_receipt', note='reviewed visible receipt total').
- Options: payment_option_52 full_payment 39660x1 from 2024-09-04 total 39660; payment_option_53 installments 20623.2x2 from 2024-09-04 total 41246.4; payment_option_54 installments 14013.2x3 from 2024-09-10 total 42039.6.

## request_20 — 90-day forecast
- First difference: `amount_safe_to_pay`; all: amount_safe_to_pay, decision_explanation.
- Expected: `5400 | not_affordable | not_recommended | none |  | none`.
- Current: `32935.01 | not_affordable | not_recommended | none |  | none`.
- Profile: start `102609.05` INR; minimum `64500`; methods `full_payment|partial_payment|installments`; deadline `2026-02-22`.
- Income evidence: event_1717 salary/credit 108000 settled 2025-11-15; event_1725 salary/credit 108000 settled 2025-12-15; event_1733 salary/credit 108000 settled 2026-01-15; event_1785 shopping/credit 8640 pending 2026-02-14.
- Expense evidence: event_1779 dining/debit 2857.78 settled 2025-11-07; event_1780 dining/debit 4308.23 settled 2025-11-28; event_1781 dining/debit 2629.91 settled 2025-12-19; event_1782 dining/debit 3352.75 settled 2026-01-09; event_1783 dining/debit 3803.95 settled 2026-01-30; event_1784 shopping/debit 8640 settled 2026-01-15; event_1786 utilities/debit 704.05 pending 2026-02-09; event_1787 shopping/debit 4470 pending 2026-02-08.
- Recurrence candidates: cloud_storage: event_1724,event_1732,event_1740; dining: event_1781,event_1782,event_1783; education: event_1721,event_1729,event_1737; entertainment: event_1723,event_1731,event_1739; groceries: event_1759,event_1760,event_1761; healthcare: event_1722,event_1730,event_1738; housing: event_1726,event_1734,event_1741; insurance: event_1728,event_1736,event_1743; salary: event_1717,event_1725,event_1733; shopping: event_1784,event_1787; transport: event_1772,event_1773,event_1774; utilities: event_1735,event_1742,event_1786.
- Pending/scheduled: event_1785 shopping/credit 8640 pending 2026-02-14; event_1786 utilities/debit 704.05 pending 2026-02-09; event_1787 shopping/debit 4470 pending 2026-02-08.
- Messages: CartLane has new information about your payment or refund. Your refund has been initiated but has not reached your account yet. We’ll send a.
- Image evidence: image_05 -> Extraction(amount=Decimal('704.05'), confidence='reviewed', source='reviewed_receipt', note='reviewed visible receipt total').
- Options: payment_option_55 full_payment 303700x1 from 2026-02-07 total 303700; payment_option_56 installments 19234.33x18 from 2026-02-07 total 346217.94.

## request_21 — recurrence handling / spending-change logic
- First difference: `amount_safe_to_pay`; all: amount_safe_to_pay, affordability_status, payment_plan, earliest_date_for_full_payment, spending_changes_needed, decision_explanation.
- Expected: `1543.35 | affordable_with_plan | full_payment | 2026-04-03:1574.40 | 2026-04-15 | stop:event_1815|reduce_to:event_1816:23.50`.
- Current: `1574.4 | affordable_now | full_payment | 2026-04-03:1574.4 | 2026-04-03 | none`.
- Profile: start `3911.35` USD; minimum `1800`; methods `full_payment`; deadline `2026-04-14`.
- Income evidence: event_1800 salary/credit 2256 settled 2026-01-15; event_1806 salary/credit 2256 settled 2026-02-15; event_1812 salary/credit 2256 settled 2026-03-15; event_1858 salary/credit 2256 scheduled 2026-04-15.
- Expense evidence: event_1849 dining/debit 60.18 settled 2025-12-12; event_1850 dining/debit 88.07 settled 2026-01-02; event_1851 dining/debit 100.63 settled 2026-01-23; event_1852 dining/debit 97.67 settled 2026-02-13; event_1853 dining/debit 98.39 settled 2026-03-06; event_1854 dining/debit 69.31 settled 2026-03-27; event_1855 investment/debit 676.8 settled 2025-12-29; event_1857 transport/debit 53 pending 2026-04-05.
- Recurrence candidates: cloud_storage: event_1803,event_1809,event_1815; dining: event_1852,event_1853,event_1854; groceries: event_1834,event_1835,event_1836; rent: event_1807,event_1813,event_1818; salary: event_1806,event_1812,event_1858; shopping: event_1805,event_1811,event_1817; streaming: event_1804,event_1810,event_1816; transport: event_1844,event_1845,event_1857; utilities: event_1802,event_1808,event_1814.
- Pending/scheduled: event_1857 transport/debit 53 pending 2026-04-05; event_1858 salary/credit 2256 scheduled 2026-04-15.
- Messages: none.
- Image evidence: none.
- Options: payment_option_57 full_payment 1574.4x1 from 2026-04-03 total 1574.4; payment_option_58 installments 88.47x21 from 2026-04-06 total 1857.87; payment_option_59 installments 283.39x6 from 2026-04-10 total 1700.34; payment_option_60 installments 80.03x24 from 2026-04-17 total 1920.72.

## request_22 — 90-day forecast / earliest-full-payment calculation
- First difference: `amount_safe_to_pay`; all: amount_safe_to_pay, earliest_date_for_full_payment, decision_explanation.
- Expected: `475.46 | affordable_with_plan | installments | 2024-12-08:253.59|2025-01-05:253.59|2025-02-02:253.59 | 2025-01-15 | none`.
- Current: `572.47 | affordable_with_plan | installments | 2024-12-08:253.59|2025-01-05:253.59|2025-02-02:253.59 | 2024-12-16 | none`.
- Profile: start `1132.46` EUR; minimum `500`; methods `installments`; deadline `2025-02-10`.
- Income evidence: event_1866 salary/credit 616 settled 2024-08-15; event_1873 salary/credit 616 settled 2024-09-15; event_1880 salary/credit 616 settled 2024-10-15; event_1887 salary/credit 616 settled 2024-11-15.
- Expense evidence: event_1953 dining/debit 16.03 settled 2024-09-20; event_1954 dining/debit 14.22 settled 2024-10-04; event_1955 dining/debit 18.53 settled 2024-10-18; event_1956 dining/debit 12.65 settled 2024-11-01; event_1957 dining/debit 15.84 settled 2024-11-15; event_1958 dining/debit 18.41 settled 2024-11-29; event_1959 investment/debit 184.8 settled 2024-09-01; event_1961 shopping/debit 43 pending 2024-12-08.
- Recurrence candidates: delivery_membership: event_1877,event_1884,event_1891; dining: event_1956,event_1957,event_1958; entertainment: event_1879,event_1886,event_1893; groceries: event_1918,event_1919,event_1920; gym: event_1878,event_1885,event_1892; music_subscription: event_1876,event_1883,event_1890; rent: event_1881,event_1888,event_1894; salary: event_1873,event_1880,event_1887; transport: event_1943,event_1944,event_1945; utilities: event_1875,event_1882,event_1889.
- Pending/scheduled: event_1961 shopping/debit 43 pending 2024-12-08.
- Messages: Here’s the latest account information from ClearFund. Your portfolio’s displayed market value has increased substantially. No units have bee.
- Image evidence: none.
- Options: payment_option_61 installments 253.59x3 from 2024-12-08 total 760.77; payment_option_62 full_payment 731.5x1 from 2024-12-05 total 731.5; payment_option_63 installments 53.64x15 from 2024-12-12 total 804.6.

## request_23 — 90-day forecast / earliest-full-payment calculation
- First difference: `amount_safe_to_pay`; all: amount_safe_to_pay, payment_plan, earliest_date_for_full_payment, decision_explanation.
- Expected: `9152 | affordable_later | wait | 2025-07-15:38016 | 2025-07-15 | none`.
- Current: `23404.71 | affordable_later | wait | 2025-05-16:38016 | 2025-05-16 | none`.
- Profile: start `51957.9` ZAR; minimum `27000`; methods `full_payment|partial_payment|installments`; deadline `2025-07-15`.
- Income evidence: event_1970 salary/credit 45760 settled 2025-01-15; event_1978 salary/credit 45760 settled 2025-02-15; event_1986 salary/credit 45760 settled 2025-03-15; event_1994 salary/credit 45760 settled 2025-04-15.
- Expense evidence: event_2035 transport/debit 1046.56 settled 2025-02-20; event_2036 transport/debit 738.21 settled 2025-03-06; event_2037 transport/debit 956.01 settled 2025-03-20; event_2038 transport/debit 1092.98 settled 2025-04-03; event_2039 transport/debit 834 settled 2025-04-17; event_2040 transport/debit 783.18 settled 2025-05-01; event_2041 investment/debit 13728 settled 2025-02-01; event_2042 healthcare/debit 1553.2 pending 2025-05-11.
- Recurrence candidates: cloud_storage: event_1984,event_1992,event_2000; debt_repayment: event_1981,event_1989,event_1997; family_support: event_1983,event_1991,event_1999; groceries: event_2025,event_2026,event_2027; healthcare: event_1990,event_1998,event_2042; rent: event_1987,event_1995,event_2002; salary: event_1978,event_1986,event_1994; shopping: event_1985,event_1993,event_2001; transport: event_2038,event_2039,event_2040; utilities: event_1980,event_1988,event_1996.
- Pending/scheduled: event_2042 healthcare/debit 1553.2 pending 2025-05-11.
- Messages: Here’s the latest account information from DrawPay. Your prize claim has been verified and is still in payment processing. The payment has n.
- Image evidence: none.
- Options: payment_option_64 full_payment 38016x1 from 2025-05-07 total 38016; payment_option_65 installments 2407.68x18 from 2025-05-21 total 43338.24; payment_option_66 installments 1932.48x24 from 2025-05-10 total 46379.52.

## request_24 — 90-day forecast
- First difference: `amount_safe_to_pay`; all: amount_safe_to_pay, decision_explanation.
- Expected: `13420 | not_affordable | not_recommended | none |  | none`.
- Current: `3974.49 | not_affordable | not_recommended | none |  | none`.
- Profile: start `85045` INR; minimum `51000`; methods `partial_payment`; deadline `2026-02-08`.
- Income evidence: event_2059 salary/credit 61000 settled 2025-10-15; event_2067 salary/credit 61000 settled 2025-11-15; event_2075 salary/credit 61000 settled 2025-12-15; event_2165 windfall/credit 33550 settled 2025-12-28.
- Expense evidence: event_2158 dining/debit 1415.29 settled 2025-11-29; event_2159 dining/debit 1842.2 settled 2025-12-06; event_2160 dining/debit 1911.68 settled 2025-12-13; event_2161 dining/debit 2184.47 settled 2025-12-20; event_2162 dining/debit 2151.71 settled 2025-12-27; event_2163 dining/debit 1918.02 settled 2026-01-03; event_2164 investment/debit 18300 settled 2025-10-01; event_2166 insurance/debit 1830 scheduled 2026-01-11.
- Recurrence candidates: cloud_storage: event_2063,event_2071,event_2079; dining: event_2161,event_2162,event_2163; entertainment: event_2066,event_2074,event_2082; groceries: event_2099,event_2100,event_2101; insurance: event_2070,event_2078,event_2166; rent: event_2068,event_2076,event_2083; salary: event_2059,event_2067,event_2075; shopping: event_2065,event_2073,event_2081; streaming: event_2064,event_2072,event_2080; transport: event_2135,event_2136,event_2137; utilities: event_2061,event_2069,event_2077.
- Pending/scheduled: event_2166 insurance/debit 1830 scheduled 2026-01-11.
- Messages: Here’s the latest account information from PrizeTrack. The prize proceeds have reached your account after withholding. The claim is now clos.
- Image evidence: none.
- Options: payment_option_67 full_payment 109600x1 from 2026-01-04 total 109600; payment_option_68 installments 6158.48x21 from 2026-01-04 total 129328.08.

## request_25 — 90-day forecast
- First difference: `amount_safe_to_pay`; all: amount_safe_to_pay, decision_explanation.
- Expected: `1425000 | not_affordable | not_recommended | none |  | none`.
- Current: `7349230.12 | not_affordable | not_recommended | none |  | none`.
- Profile: start `32063050` IDR; minimum `23379100`; methods `full_payment|installments`; deadline `2024-04-17`.
- Income evidence: event_2183 salary/credit 1800 settled 2023-12-15; event_2191 salary/credit 1800 settled 2024-01-15; event_2199 salary/credit 1800 settled 2024-02-15; event_2288 salary/credit 1800 scheduled 2024-03-15.
- Expense evidence: event_2280 dining/debit 1204804.45 settled 2024-01-17; event_2281 dining/debit 1057617.64 settled 2024-01-24; event_2282 dining/debit 1251981.8 settled 2024-01-31; event_2283 dining/debit 949118.03 settled 2024-02-07; event_2284 dining/debit 1051249.87 settled 2024-02-14; event_2285 dining/debit 777034.83 settled 2024-02-21; event_2286 dining/debit 1133036.68 settled 2024-02-28; event_2287 utilities/debit 1246400 failed 2024-03-04.
- Recurrence candidates: cloud_storage: event_2187,event_2195,event_2203; dining: event_2284,event_2285,event_2286; entertainment: event_2190,event_2198,event_2206; groceries: event_2223,event_2224,event_2225; insurance: event_2186,event_2194,event_2202; rent: event_2192,event_2200,event_2207; salary: event_2191,event_2199,event_2288; shopping: event_2189,event_2197,event_2205; streaming: event_2188,event_2196,event_2204; transport: event_2259,event_2260,event_2261; utilities: event_2193,event_2201,event_2287.
- Pending/scheduled: event_2288 salary/credit 1800 scheduled 2024-03-15.
- Messages: none.
- Image evidence: none.
- Options: payment_option_69 full_payment 60496000x1 from 2024-03-06 total 60496000; payment_option_70 installments 4436373.33x15 from 2024-03-09 total 66545599.95; payment_option_71 installments 3075213.33x24 from 2024-03-20 total 73805119.92.

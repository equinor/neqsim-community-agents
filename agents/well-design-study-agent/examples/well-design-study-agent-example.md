# Well Design Study Agent Example

Request: screening design check of a synthetic 3 500 m vertical exploration well in 370 m of water.

Run `skills/subsurface/neqsim-well-design-study/examples/example_study.py`: it builds a pressure model, checks three sections against the window and kick tolerance, selects casing strings (20 in L80, 13-3/8 in L80, 9-5/8 in P110) and returns a time and cost P10/P50/P90 range. The built-in 9-5/8 in 47 ppf N80 rating check passes. Result label: SCREENING_READY_FOR_HUMAN_REVIEW.

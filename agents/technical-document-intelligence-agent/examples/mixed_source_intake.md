# Mixed-source intake example

Input set:

- a digital equipment datasheet PDF;
- a scanned P&ID PDF;
- an XLSX line list;
- a photograph of an equipment nameplate.

Expected routing:

1. Extract native PDF text/tables and render visual pages.
2. OCR and visually interpret the scanned P&ID.
3. retain workbook sheets, cells, headers, formulas, and units.
4. OCR and visually inspect the nameplate image.
5. Package every engineering fact with source/page or cell, original text, confidence, and review status.
6. Report contradictory tag, pressure, temperature, material, or revision values before downstream use.

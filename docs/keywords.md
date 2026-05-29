# Keywords File --- Version 1.0

File exported from external Keyword Management system, JSON format.\
Default file path: `~/Google Drive/My Drive/Biz/Keywords/keywords.json`

## Notes

-   Parts of the path may be links (shortcuts) to shared folders. Some
    software parses them incorrectly (Finder --- OK).

-   Python requires preprocessing:

    ``` python
    expanded_path = os.path.expanduser(path_str)
    ```

## Structure

The file has two main parts: **meta** and **data**.

### Meta

General info and XMP data.

### Data

Contains three sections:

-   **items** --- keywords to describe items\
-   **themes** --- keywords for themes (e.g. Christmas)\
-   **types** --- keywords to describe result image types (e.g. coloring
    page, isolated vector items)

------------------------------------------------------------------------

## JSON Example

``` json
{
  "meta": {
    "creationDate": "Mon, 23 Mar 2026 16:29:11 GMT",
    "creator": "Ksenya Savva",
    "webStatement": "http://savva.club",
    "rights": "Copyright © 2026 Ksenya Savva",
    "XMPNSPrefix": "ID_keywords:",
    "XMPUserNamespace": "http://savva.club/keywords/1.0/"
  },
  "data": {
    "items": {
      "Rose": {
        "id": "Rose",
        "mainKeywords": [
          "rose",
          "gift",
          "valentine",
          "red",
          "birthday",
          "february"
        ],
        "optionalKeywords": [
          "symbol",
          "single",
          "thorn",
          "bud",
          "fresh"
        ]
      },
      "Poppy": {
        "id": "Poppy",
        "mainKeywords": [
          "poppy",
          "red"
        ],
        "optionalKeywords": []
      },
      "Apple tree": {
        "id": "Apple tree",
        "mainKeywords": [
          "apple",
          "tree",
          "green",
          "fruit",
          "red",
          "food",
          "branch",
          "garden",
          "leaf",
          "growth",
          "harvest",
          "season",
          "autumn",
          "nature",
          "summer",
          "wood",
          "farm"
        ],
        "optionalKeywords": []
      }
    },
    "themes": {
      "Flowers": {
        "id": "Flowers",
        "mainKeywords": [
          "flower",
          "nature",
          "garden",
          "blossom",
          "summer",
          "leaf",
          "botany",
          "flora",
          "decor",
          "bouquet",
          "field",
          "meadow",
          "floral",
          "beautiful",
          "beauty",
          "petal",
          "romantic",
          "love",
          "wedding",
          "bloom",
          "spring",
          "delicate"
        ],
        "optionalKeywords": []
      }
    },
    "types": {
      "Coloring book": {
        "id": "Coloring book",
        "mainKeywords": [
          "book",
          "page",
          "outline",
          "activity",
          "coloring",
          "coloration",
          "illustration",
          "painting",
          "colorless",
          "black",
          "white",
          "education",
          "game",
          "black and white"
        ],
        "optionalKeywords": [
          "isolated",
          "vector",
          "child",
          "toy",
          "kid",
          "printable",
          "worksheet",
          "preschool",
          "kindergarten"
        ]
      }
    }
  }
}
```

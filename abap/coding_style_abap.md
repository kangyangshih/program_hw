# coding style 和命名規則

從靈活簡潔的 Python 轉到嚴謹、甚至帶點「古典型藝術感」的 ABAP，命名規則的邏輯會完全不同。

ABAP 更加強調**作用域（Scope）**與**資料類型（Data Type）**的識別。

在 SAP 開發社群中，最主流的規範是 **Clean ABAP**，以下為你整理的命名規則與風格指南：

---

## 1. 命名規則 (Naming Conventions)

ABAP 的命名通常採用 **「前綴 (Prefix)」** 邏輯，讓你一眼就能看出變數的性質。

### 變數命名 (Prefix Logic)

格式通常為：`[作用域][類型]_[名稱]`

| 前綴 | 意義 | 範例 |
| --- | --- | --- |
| `lv_` | **L**ocal **V**ariable (區域變數) | `lv_user_id` |
| `gv_` | **G**lobal **V**ariable (全域變數) | `gv_total_amount` |
| `ls_` | **L**ocal **S**tructure (區域結構) | `ls_address` |
| `lt_` | **L**ocal **T**able (區域內表) | `lt_flight_list` |
| `lo_` | **L**ocal **O**bject (區域物件/實例) | `lo_processor` |
| `lr_` | **L**ocal **R**eference (區域引用/指標) | `lr_data` |

### 函式與方法參數 (Procedure Parameters)

為了區分進入與出去的資料，參數前綴至關重要：

* **`iv_`** (Importing Variable): 傳入參數。
* **`ev_`** (Exporting Variable): 傳出參數。
* **`cv_`** (Changing Variable): 修改參數。
* **`rv_`** (Returning Variable): 回傳值（用於 Method）。

---

## 2. 物件與開發物件命名 (Global Objects)

在 SAP 系統中，所有自定義物件必須以 **Z** 或 **Y** 開頭：

* **類別 (Classes)**: `ZCL_` 或 `ZCX_` (異常類別)。例如：`ZCL_SALES_ORDER`。
* **介面 (Interfaces)**: `ZIF_`。例如：`ZIF_PRINTABLE`。
* **程式 (Reports)**: `Z` + 模組縮寫 + 描述。例如：`ZRFI_POST_DOCUMENT`。

---

## 3. 代碼撰寫風格 (Coding Style)

### 關鍵字大小寫

雖然 ABAP 不區分大小寫，但為了可讀性：

* **關鍵字大寫**：`SELECT`, `IF`, `LOOP`, `ENDIF`.
* **變數小寫**：`lv_count`, `lt_table`.

> *註：現代開發工具 (ADT) 通常會自動處理這個部分。*

### 縮排與空行

* **縮排**：一律使用 **2 個空格**（由系統 Pretty Printer 自動排版）。
* **鏈接語句 (Chained Statements)**：使用冒號 `:` 來簡化重複的關鍵字。
```abap
" 不推薦
DATA lv_a TYPE i.
DATA lv_b TYPE i.

" 推薦
DATA: lv_a TYPE i,
      lv_b TYPE i.

```



### 註解 (Comments)

* **全行註解**：在行首使用星號 `*`。
* **行尾註解**：使用雙引號 `"`。

---

## 4. 現代化 ABAP (Clean ABAP) 建議

隨著 SAP 推行 **ABAP 7.40/7.50+**，風格越來越接近現代語言：

1. **盡量使用 Inline Declaration (內聯聲明)**：
不需要在程式開頭宣告一堆 `DATA`，在使用時直接宣告。
```abap
" 舊寫法
DATA lv_text TYPE string.
lv_text = 'Hello'.

" 新寫法 (推薦)
DATA(lv_text) = 'Hello'.

```


2. **優先使用方法 (Methods) 而非子程序 (Subroutines)**：
盡量少用 `PERFORM / FORM`，改用類別方法。
3. **避免過時語法**：
* 使用 `&&` 代替 `CONCATENATE`。
* 使用 `NEW` 代替 `CREATE OBJECT`。


---

## 5. 實踐範例

這是一個符合規範的簡單 Method 寫法：

```abap
METHOD get_user_status.
  " 導入口參數 iv_user_id
  " 回傳值 rv_status

  SELECT SINGLE status 
    FROM zuser_table 
    WHERE user_id = @iv_user_id 
    INTO @DATA(lv_current_status).

  IF sy-subrc = 0.
    rv_status = lv_current_status.
  ELSE.
    " 異常處理
  ENDIF.
ENDMETHOD.

```

**小撇步：** 在 SAP GUI 裡，記得點擊工具列上的 **"Pretty Printer"** 按鈕，它會根據你的設定自動把縮排跟大小寫校正過來！

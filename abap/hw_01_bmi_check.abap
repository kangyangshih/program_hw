REPORT ZHW_01_BMI_CHECK.

PARAMETERS:
  p_height TYPE decfloat16 DEFAULT '170',
  p_weight TYPE decfloat16 DEFAULT '60'.

DATA:
  lv_height_m TYPE decfloat16,
  lv_bmi      TYPE decfloat16.

START-OF-SELECTION.

  lv_height_m = p_height / 100.

  IF lv_height_m = 0.
    WRITE: / 'Height cannot be zero'.
    RETURN.
  ENDIF.

  lv_bmi = p_weight / ( lv_height_m * lv_height_m ).

  WRITE: / 'BMI =', lv_bmi.
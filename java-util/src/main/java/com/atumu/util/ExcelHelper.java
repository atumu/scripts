package com.atumu.util;

import org.apache.commons.lang3.StringUtils;
import org.apache.poi.hssf.usermodel.HSSFDateUtil;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.joda.time.DateTime;

/**
 * @author: zhangl
 * @date: 2017/2/9
 * @time: 11:12
 * @description: excel帮助类
 */
public class ExcelHelper {

    /**
     * 获取单元格值(字符串格式)
     *
     * @param row   一行数据
     * @param index 目标单元格角标
     * @return 单元格内容(字符)
     */
    public static String getStringCellValue(Row row, int index) {
        return helper(getString(row, index, ""));
    }

    /**
     * 获取单元格值(字符串格式)
     *
     * @param row          一行数据
     * @param index        目标单元格角标
     * @param defaultValue 默认值
     * @return 单元格内容(字符)
     */
    public static String getStringCellValue(Row row, int index, String defaultValue) {
        return helper(getString(row, index, defaultValue));
    }

    private static String helper(String src) {
        return src.replaceAll("\\(", "（").replaceAll("\\)", "）").replaceAll("\n", "").replaceAll("—", "-").trim();
    }

    /**
     * 获取单元格值(字符串格式)
     *
     * @param row          一行数据
     * @param index        目标单元格角标
     * @param defaultValue 默认值
     * @return 单元格内容(字符)
     */
    private static String getString(Row row, int index, String defaultValue) {
        Cell cell = row.getCell(index);
        if (cell == null
            || (cell.getCellType() == Cell.CELL_TYPE_STRING && StringUtils.isBlank(cell
            .getStringCellValue()))) {
            return defaultValue;
        }
        int cellType = cell.getCellType();
        switch (cellType) {
            case Cell.CELL_TYPE_BLANK:
                return defaultValue;
            case Cell.CELL_TYPE_BOOLEAN:
                return String.valueOf(cell.getBooleanCellValue());
            case Cell.CELL_TYPE_ERROR:
                return String.valueOf(cell.getErrorCellValue());
            case Cell.CELL_TYPE_FORMULA:
                return String.valueOf(cell.getNumericCellValue());
            case Cell.CELL_TYPE_NUMERIC:
                if (HSSFDateUtil.isCellDateFormatted(cell)) {
                    return new DateTime(cell.getDateCellValue()).toString("yyyy/MM/dd");
                } else {
                    cell.setCellType(Cell.CELL_TYPE_STRING);
                    return String.valueOf(cell.getStringCellValue());
                }
            case Cell.CELL_TYPE_STRING:
                return cell.getStringCellValue();
            default:
                return defaultValue;
        }
    }

    /**
     * convert Excel Index to Arabic
     *
     * @param index 0<i<676
     * @return 阿拉伯
     */
    public static String convertIndexToABC(int index) {
        String[] rs = { "", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
            "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" };
        int quotient = index / 26;
        int remainder = index % 26;
        quotient = remainder == 0 ? (quotient > 0 ? quotient - 1 : 0) : quotient;
        return rs[quotient] + rs[remainder == 0 ? 26 : remainder];
    }

    public static void main(String[] args) {
        System.out.println(convertIndexToABC(1));
        System.out.println(convertIndexToABC(4));
        System.out.println(convertIndexToABC(26));
        System.out.println(convertIndexToABC(27));
        System.out.println(convertIndexToABC(29));
        System.out.println(convertIndexToABC(52));
        System.out.println(convertIndexToABC(53));
        System.out.println(convertIndexToABC(676));
        System.out.println(convertIndexToABC(677));
    }
}

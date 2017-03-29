package com.atumu.util;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.apache.commons.beanutils.BeanUtils;
import org.apache.commons.lang3.StringUtils;

public class BeanHelper<T> {


    /**
     * 对比两个对象的属性值
     *
     * @param origin  源对象
     * @param target  目标对象
     * @param ignores 可忽略字段
     * @param log     重写类型类对象
     * @return 修改的字段
     * @throws Exception 反射异常
     */
    public List compare(T origin,
                           T target,
                           List<String> ignores,
                           Object log) throws Exception {
        List logs = new ArrayList();
        if (origin != null && target != null) {
            try {
                Map<String, String> orignMap = BeanUtils.describe(origin);
                Map<String, String> targetMap = BeanUtils.describe(target);
                for (Map.Entry<String, String> entry : orignMap.entrySet()) {
                    String key = entry.getKey();
                    if (ignores != null && ignores.contains(key)) {
                        continue;
                    }
                    String originValue = entry.getValue();
                    String targetValue = targetMap.get(key);

                    if ((StringUtils.isBlank(originValue) && StringUtils.isNotBlank(targetValue)) ||
                        (StringUtils.isNotBlank(originValue) && !originValue.equals(targetValue))) {
                        // TODO 记录
                        //log.setParam(key);
                        //log.setSource(originValue);
                        //log.setTarget(targetValue);
                        //logs.add(log.clone());
                    }
                }
            } catch (Exception e) {
                e.printStackTrace();
                throw new Exception("对比两个对象的属性值-反射异常", e);
            }
        }
        return logs;
    }

}
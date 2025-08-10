---
layout: default
title: "AI Tool을 사용하는 초보개발자를위한 조언 # 1"
date: 2025-08-09
category: "블로그"
description: ""
cache-control: no-cache
expires: 0
pragma: no-cache
---

# AI Tool을 사용하는 초보개발자를위한 조언 # 1

- **오류 대응**: 에러가 발생해도 당황하지 말고 차분히 대처하세요.

- **검토 습관**: AI에 맡기기 전에 코드를 미리 검토하고, 문제점을 스스로 고민해보세요.

- **효율적인 협업**: 필요할 때 AI에게 수정을 요청하고, 결과물이 자신의 의도와 일치하는지 비교하세요.

- **역량 개발**: 간단한 오류는 직접 수정하는 습관을 들이고, 복잡한 문제는 AI의 도움을 받아 오타를 줄이세요.

예)

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

lasso_model = Lasso(alpha=1, max_iter=2000, normalize=True)
lasso_mode.fit(X_train, y_train)  # 🚨 오타: lasso_mode -> lasso_model

y_train_predict = lasso_model.predict(X_train)
y_test_predict = lasso_model.predict(X_test)
```

```
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-1-94f22914643a> in <module>
     30 
     31 lasso_model = Lasso(alpha=1, max_iter=2000, normalize=True)
---> 32 lasso_mode.fit(X_train, y_train)
     33 
     34 y_train_predict = lasso_model.predict(X_train)

NameError: name 'lasso_mode' is not defined
```
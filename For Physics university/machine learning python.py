#import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#بارگذاری داده های اولیه از روی فایل ایکسل 
data = pd.read_csv('./exl.csv')
x = data.drop('label' , axis=1)
y = data['label']

#تقسیم داده ها به مجموعه های آموزشی و آزمایشی
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#آموزش مدل یادگیری ماشین SVM
clf = SVC(kernel='linear')
clf.fit(x_train, y_train)

#ارزیابی دقت تشخیص مدل ساخته شده بر روی مجموعه های تست
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

#مصور سازی خط تصمیم گیری بر روی صفحه دو بعدی 
fig, ax = plt.subplots()
ax.scatter(X_train['Height'], X_train['Speed'], c=y_train, cmap='coolwarm')
xlim = ax.get_xlim()
ylim = ax.get_ylim()

#ایجاد خط منش برای ترسیم مرز داده ها 
xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 50), np.linspace(ylim[0], ylim[1], 50))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel(), np.zeros(xx.ravel().shape), np.zeros(xx.ravel().shape), np.zeros(xx.ravel().shape), np.zeros(xx.ravel().shape), np.zeros(xx.ravel().shape)])

#مصور سازی خط مش ایجاد شده
z = z.rashape(xx.shape)
ax.contourf(xx, yy, Z, alpha=0.5, camp='coolwarm')
ax.set_xlim(xlim)
ax.set_ylim(ylim)
ax.set_xlabel('Height')
ax.set_ylabel('Speed')
ax.set_title('SVM Decision Boundary in 2D')

#مصور سازی خط تصمیم گیری بر روی صفحه سه بعدی 
fig_3d = plt.figure()
ax_3d = fig_3d.add_subplot(111, projection='3d')
ax_3d.scatter(X_train['Height'], x_train['Speed'], x_train['Angle'], c=y_train, cmap='coolwarm')
xlim_3d = ax_3d.get_xlim()
ylim_3d = ax_3d.get_ylim()
zlim_3d = ax_3d.get_zlim()

#ایجاد خط مش برای ترسیم مرز داده ها 
xx_3d, yy_3d = np.meshgrid(np.linspace(xlim_3d[0], xlim_3d[1], 10), np.linspace(ylim_3d[0], ylim_3d[1], 10))
zz_3d = (-clf.intercept_[0] - clf.coef_[0][0] * xx_3d - clf.coef[0][1] * yy_3d) / clf.coef_[0][2]

#مصور سازی خط مش ایجاد شده در داده ها 
ax_3d.plot_surface(xx_3d, yy_3d, zz_3d, alpha=0.5)
ax_3d.set_xlim(xlim_3d) 
ax_3d.set_ylim(ylim_3d)
ax_3d.set_zlim(zlim_3d)
ax_3d.set_xlabel('Height')
ax_3d.set_ylabel('Speed')
ax_3d.set_zlabel('Angle')
ax_3d.set_title('SVM Decision Boundary in 3D')
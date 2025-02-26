TEMPLATE = app
CONFIG += console
CONFIG -= app_bundle

QT += widgets
QT += network


# Ajout de cUrl à la configuration
# cUrl ==> création de requêtes HTTP personnalisés
INCLUDEPATH += /usr/include
LIBS += -lcurl

SOURCES += \
    createutil.cpp \
    main.cpp \
    monitorhousedata.cpp \
    window.cpp

HEADERS += \
    createutil.h \
    monitorhousedata.h \
    window.h


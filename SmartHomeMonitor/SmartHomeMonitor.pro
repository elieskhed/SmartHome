TEMPLATE = app
CONFIG += console
CONFIG -= app_bundle

QT += widgets
QT += network
QT += charts


# Ajout de cUrl à la configuration
# cUrl ==> création de requêtes HTTP personnalisés
INCLUDEPATH += /usr/include
LIBS += -lcurl

SOURCES += \
    apiresponseparser.cpp \
    createutil.cpp \
    main.cpp \
    monitorhousedata.cpp \
    window.cpp

HEADERS += \
    apiresponseparser.h \
    createutil.h \
    monitorhousedata.h \
    window.h


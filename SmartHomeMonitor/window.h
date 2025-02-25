#ifndef WINDOW_H
#define WINDOW_H

#include <QMainWindow>
#include <QWidget>
#include <QMenu>
#include <QMenuBar>
#include <QAction>
#include <QTabWidget>

#include "createutil.h"
#include "monitorhousedata.h"

class Window : public QMainWindow
{
    Q_OBJECT
public:
    Window(int width, int height);

private:
    int width;
    int height;


    QMenu* fileMenu;
    QAction* quitAction;

    QWidget* centralWidget;

    CreateUtil* createUtilWidget;
    MonitorHouseData* monitorHouseDataWidget;

signals:
    void quitRequested();


};

#endif // WINDOW_H

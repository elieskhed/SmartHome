#include <QApplication>
#include <QWidget>
#include <QPushButton>
#include "window.h"

int main(int argc, char* argv[]){

    QApplication app(argc, argv);

    Window* window = new Window(800, 900);
    window->show();

    return app.exec();
}

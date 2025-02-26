#include "window.h"

Window::Window(int width, int height):
    width(width),
    height(height)
{

    // Création des onglets
    QTabWidget* onglets = new QTabWidget(this);
    onglets->setGeometry(0, 0, this->width, this->height);

    this->createUtilWidget = new CreateUtil();
    this->monitorHouseDataWidget = new MonitorHouseData();

    // Chaque Classe représente une fonctionnalité de l'API
    // modélisé par un widget
    onglets->addTab(this->createUtilWidget, "Créer une Maison");
    onglets->addTab(this->monitorHouseDataWidget, "Surveiller une maison");

   // this->centralWidget = new QWidget(this);
    //this->setCentralWidget(this->centralWidget);

    this->setFixedSize(this->width, this->height);
    this->setWindowTitle("SmartHome Monitor");



    this->fileMenu = menuBar()->addMenu("&Fichier");
    this->quitAction = new QAction("Quitter", this);
    this->fileMenu->addAction(quitAction);



    //connect(quitAction, SIGNAL(clicked()), this, SLOT(quit()));


}

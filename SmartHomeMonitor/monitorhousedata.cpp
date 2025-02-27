#include "monitorhousedata.h"

#define URL "172.20.10.5"
#define PORT 80

MonitorHouseData::MonitorHouseData() {
    QLabel* labelHouseToken = new QLabel("Token de la maison");
    this->houseToken = new QTextEdit();
    this->houseToken->setFixedSize(750, 50);

    this->checkBoxLastData = new QCheckBox("last data", this);
    this->checkBoxDataFromScratch = new QCheckBox("data from scratch", this);

    this->buttonSend = new QPushButton("Etats du capteur");

    this->verticalLayout = new QVBoxLayout();
    this->verticalLayout->addWidget(labelHouseToken);
    this->verticalLayout->addWidget(this->houseToken);
    this->verticalLayout->addWidget(this->checkBoxLastData);
    this->verticalLayout->addWidget(this->checkBoxDataFromScratch);
    this->verticalLayout->addWidget(this->buttonSend);

    QObject::connect(this->buttonSend, &QPushButton::clicked, [this](){
        this->connectAPILastData();
    });

    //mise en place du graphique example
    this->createChartsExample();
    this->verticalLayout->addWidget(this->chartView);

    this->setLayout(this->verticalLayout);
}



void MonitorHouseData::connectAPILastData() {
    // gestionnaire de requêtes réseau
    QNetworkAccessManager *manager = new QNetworkAccessManager();

    QUrl url("http://172.20.10.5:8000/api/house/latestData?token=Wdp4HCPNvC3wHnvSfSwmVknhLuHtjUkoIzG6zPno");
    QNetworkRequest request(url);

    // Envoi de la requête GET
    QNetworkReply *reply = manager->get(request);

    // Connexion du signal finished pour traiter la réponse dès réception
    QObject::connect(reply, &QNetworkReply::finished, [reply, manager]() {
        if (reply->error() == QNetworkReply::NoError) {
            QByteArray responseData = reply->readAll();
            qDebug() << "Réponse de l'API:" << responseData;
        } else {
            qDebug() << "Erreur lors de la requête:" << reply->errorString();
        }
        reply->deleteLater();
        manager->deleteLater();
    });
}


void MonitorHouseData::createChartsExample(){
    this->series = new QLineSeries;


    this->chart = new QChart();
    this->chart->legend()->hide();
    this->chart->addSeries(series);
    this->chart->createDefaultAxes();
    this->chart->setTitle("Exemple de Graphique");

    this->chartView = new QChartView(chart);
    this->chartView->setRenderHint(QPainter::Antialiasing);

}

#include "monitorhousedata.h"

#define IP_SERV "172.20.10.5"
#define PORT 80
// token test: Wdp4HCPNvC3wHnvSfSwmVknhLuHtjUkoIzG6zPno

MonitorHouseData::MonitorHouseData() {
    QLabel* labelHouseToken = new QLabel("Token de la maison");
    this->houseToken = new QTextEdit();
    this->houseToken->setFixedSize(750, 50);

    this->checkBoxLastData = new QCheckBox("last data", this);
    this->checkBoxDataFromScratch = new QCheckBox("data from scratch", this);
    this->messageErreur = new QLabel("",this);

    this->buttonSend = new QPushButton("Etats du capteur");

    this->verticalLayout = new QVBoxLayout();
    this->verticalLayout->addWidget(labelHouseToken);
    this->verticalLayout->addWidget(this->houseToken);
    this->verticalLayout->addWidget(this->checkBoxLastData);
    this->verticalLayout->addWidget(this->checkBoxDataFromScratch);
    this->verticalLayout->addWidget(this->buttonSend);
    this->verticalLayout->addWidget(this->messageErreur);
    this->urlStr = "";

    QObject::connect(this->checkBoxLastData, &QCheckBox::toggled, this, [=](bool checked){
        if (checked){
            qDebug() << "cochée";

            if (this->houseToken->toPlainText().length() == 0){
                this->urlStr = "";
                this->messageErreur->setText("Erreur, veuillez remplir les informations nécéssaires");
                this->messageErreur->setStyleSheet("color: red; font-weight: bold;");
            }
            else {

                this->urlStr = "http://172.20.10.5:8000/api/house/latestData?token=" + this->houseToken->toPlainText();
            }


        }
        else{
            qDebug() << "decochée";
        }
    });

    QObject::connect(this->buttonSend, &QPushButton::clicked, [this](){
        if (this->urlStr.length() == 0){

            this->messageErreur->setText("Erreur lors de la création de l'url");
            this->messageErreur->setStyleSheet("color: red; font-weight: bold;");
        }
        else{
            //this->messageErreur->setText("");
            connectAPILastData(this->urlStr);
        }

    });

    //mise en place du graphique example
    this->createChartsExample();
    this->verticalLayout->addWidget(this->chartView);

    this->setLayout(this->verticalLayout);
}



void MonitorHouseData::connectAPILastData(QString const& urlStr) {
    // gestionnaire de requêtes réseau
    QNetworkAccessManager *manager = new QNetworkAccessManager();

    QUrl url(this->urlStr);
    QNetworkRequest request(url);

    // Envoi de la requête GET
    QNetworkReply *reply = manager->get(request);

    // Connexion du signal finished pour traiter la réponse dès réception
    QObject::connect(reply, &QNetworkReply::finished, [this, reply, manager]() {
        if (reply->error() == QNetworkReply::NoError) {
            QByteArray responseData = reply->readAll();
            this->responseDataStr = QString::fromUtf8(responseData);

            qDebug() << responseDataStr;
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

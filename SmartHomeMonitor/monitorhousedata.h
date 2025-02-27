#ifndef MONITORHOUSEDATA_H
#define MONITORHOUSEDATA_H

#include <QWidget>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QLabel>
#include <QtWidgets/QVBoxLayout>
#include<QtCharts/QChartView>
#include <QtCharts/QLineSeries>
#include <QtCharts/QtCharts>

#include <QNetworkAccessManager>
#include <QNetworkRequest>
#include <QNetworkReply>
#include <QUrl>
#include <QDebug>
#include <QObject>



class MonitorHouseData : public QWidget
{
    Q_OBJECT
public:
    MonitorHouseData();

    void connectAPILastData();

    void createChartsExample();


private:
    QTextEdit* houseToken;
    QPushButton* buttonSend;

    // Checkbox choix API
    QCheckBox* checkBoxLastData;
    QCheckBox* checkBoxDataFromScratch;

    QVBoxLayout* verticalLayout;

    // Graphiques QtCharts
    QLineSeries* series;
    QChart* chart;
    QChartView* chartView;


};

#endif // MONITORHOUSEDATA_H

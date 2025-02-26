#ifndef MONITORHOUSEDATA_H
#define MONITORHOUSEDATA_H

#include <QWidget>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QLabel>
#include <QtWidgets/QVBoxLayout>

class MonitorHouseData : public QWidget
{
    Q_OBJECT
public:
    MonitorHouseData();

private:
    QTextEdit* houseToken;
    QPushButton* buttonSend;

    QVBoxLayout* verticalLayout;

};

#endif // MONITORHOUSEDATA_H

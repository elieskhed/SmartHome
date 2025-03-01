#ifndef APIRESPONSEPARSER_H
#define APIRESPONSEPARSER_H

#include <QObject>
#include <QJsonObject>
#include <QJsonArray>
#include <QString>
#include <QStringList>
#include <QJsonDocument>
#include <QDebug>


class ApiResponseParser : public QObject
{
    Q_OBJECT
public:
    ApiResponseParser(QString const& jsonStr);

    void parseLastData();


private:
    QString jsonStr;
    QJsonObject jsonObj;
};

#endif // APIRESPONSEPARSER_H

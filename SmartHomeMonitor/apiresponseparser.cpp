#include "apiresponseparser.h"


ApiResponseParser::ApiResponseParser(QString const& jsonStr): jsonStr(jsonStr) {

    // Conversion de la chaine en QByteArray
    QJsonDocument doc = QJsonDocument::fromJson(this->jsonStr.toUtf8());

    // Verification que le document contient un objet JSON
    if (!doc.isObject()){
        qWarning() << "Le JSON n'est pas un objet valide";
    }

    // On récupere l'objet JSON
    //this->jsonObj = new QJsonObject();
    this->jsonObj = doc.object();

    // Extraction des valeurs

}

void ApiResponseParser::parseLastData(){

}

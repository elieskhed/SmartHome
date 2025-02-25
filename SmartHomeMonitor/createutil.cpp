#include "createutil.h"

CreateUtil::CreateUtil() {

    QLabel* labelHouseName = new QLabel("Nom de la maison");
    this->houseName = new QTextEdit();
    this->houseName->setFixedSize(750, 50);

    QLabel* labelPassword = new QLabel("Mots de passe");
    this->password = new QTextEdit();
    this->password->setFixedSize(750, 50);

    QLabel* labelConfirmPassword = new QLabel("Confirmation du mots de passe");
    this->confirmPassword = new QTextEdit();
    this->confirmPassword->setFixedSize(750, 50);

    this->buttonSend = new QPushButton("Créer un utilisateur", this);

    QLabel* labelResult = new QLabel("Résultat");
    this->result = new QTextEdit();


    this->verticalLayout = new QVBoxLayout();
    this->verticalLayout->addWidget(labelHouseName);
    this->verticalLayout->addWidget(this->houseName);
    this->verticalLayout->addWidget(labelPassword);
    this->verticalLayout->addWidget(password);
    this->verticalLayout->addWidget(labelConfirmPassword);
    this->verticalLayout->addWidget(this->confirmPassword);
    this->verticalLayout->addWidget(labelResult);
    this->verticalLayout->addWidget(this->result);
    this->verticalLayout->addWidget(this->buttonSend);

    this->setLayout(this->verticalLayout);

}

#ifndef CREATEUTIL_H
#define CREATEUTIL_H

#include <QtWidgets/QTextEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QLabel>
#include <QtWidgets/QVBoxLayout>
#include <QString>
#include <QWidget>

class CreateUtil : public QWidget
{
    Q_OBJECT
public:
    CreateUtil();

private:
    QTextEdit* houseName;
    QTextEdit* password;
    QTextEdit* confirmPassword;
    QTextEdit* result;

    QPushButton* buttonSend;

    QVBoxLayout* verticalLayout;


};

#endif // CREATEUTIL_H

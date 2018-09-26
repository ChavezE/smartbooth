#ifndef WELCOMEWINDOW_H
#define WELCOMEWINDOW_H

#include <QMainWindow>

namespace Ui {
class welcomeWindow;
}

class welcomeWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit welcomeWindow(QWidget *parent = nullptr);
    ~welcomeWindow();

private:
    Ui::welcomeWindow *ui;
};

#endif // WELCOMEWINDOW_H

#include "welcomewindow.h"
#include "ui_welcomewindow.h"

welcomeWindow::welcomeWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::welcomeWindow)
{
    ui->setupUi(this);
}

welcomeWindow::~welcomeWindow()
{
    delete ui;
}

const { app, BrowserWindow, Menu, ipcMain } = require('electron');

const url = require('url');
const path = require('path');

let mainWindow;
let newProductWindow;
let cargarPercepcion;


// Reload in Development for Browser Windows
if(process.env.NODE_ENV !== 'production') {
  require('electron-reload')(__dirname, {
    electron: path.join(__dirname, '../node_modules', '.bin', 'electron')
  });
}


app.on('ready', () => {

  // The Main Window
  mainWindow = new BrowserWindow({width: 1068, height: 840});

  mainWindow.loadURL(url.format({
    pathname: path.join(__dirname, 'views/index.html'),
    protocol: 'file',
    slashes: true
  }))

  // Menu
  const mainMenu = Menu.buildFromTemplate(templateMenu);
  // Set The Menu to the Main Window
  Menu.setApplicationMenu(mainMenu);

  // If we close main Window the App quit
  mainWindow.on('closed', () => {
    app.quit();
  });

});

//Ventana CargarRetencion
function createNewProductWindow() {
  newProductWindow = new BrowserWindow({
    width: 500,
    height: 820,
    title: 'Agregar Retemcion'
  });
  newProductWindow.setMenu(null);

  newProductWindow.loadURL(url.format({
    pathname: path.join(__dirname, 'views/nueva-retencion.html'),
    protocol: 'file',
    slashes: true
  }));
  newProductWindow.on('closed', () => {
    newProductWindow = null;
  });
}

//ventanCargaPercepcion
function crearCargarPercepcion() {
  cargarPercepcion = new BrowserWindow({
    width: 510,
    height: 820,
    title: 'Agregar Percepcion'
  });
  cargarPercepcion.setMenu(null);

  cargarPercepcion.loadURL(url.format({
    pathname: path.join(__dirname, 'views/nueva-percepcion.html'),
    protocol: 'file',
    slashes: true
  })); 
  cargarPercepcion.on('closed', () => {
    cargarPercepcion = null;
  });


}


// Ipc Renderer Events
ipcMain.on('product:new', (e, newProduct) => {
  // send to the Main Window
  console.log(newProduct);
  mainWindow.webContents.send('product:new', newProduct);
  newProductWindow.close();
});


// Menu Template
const templateMenu = [
  {
    label: 'Archivo',
    submenu: [
      {
        label: 'Nueva Retencion',
        accelerator: 'Ctrl+R',
        click() {
          createNewProductWindow();
        }
      },
      {
        label: 'Nueva Percepcion',
        accelerator: 'Ctrl+P',
        click() {
          crearCargarPercepcion();
        }
      },
      {
        label: 'Remove All Products',
        click() {
          mainWindow.webContents.send('products:remove-all');
        }
      },
      {
        label: 'Exit',
        accelerator: process.platform == 'darwin' ? 'command+Q' : 'Ctrl+Q',
        click() {
          app.quit();
        }
      }
    ]
  }
];

// if you are in Mac, just add the Name of the App
if (process.platform === 'darwin') {
  templateMenu.unshift({
    label: app.getName(),
  });
};

// Developer Tools in Development Environment
if (process.env.NODE_ENV !== 'production') {
  templateMenu.push({
    label: 'DevTools',
    submenu: [
      {
        label: 'Show/Hide Dev Tools',
        accelerator: process.platform == 'darwin' ? 'Comand+D' : 'Ctrl+D',
        click(item, focusedWindow) {
          focusedWindow.toggleDevTools();
        }
      },
      {
        role: 'reload'
      }
    ]
  })
}

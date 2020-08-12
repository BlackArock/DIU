const { ipcRenderer } = require("electron");

const fechaRetencion = document.querySelector("#fechaRetencion");
const cuitRetencion = document.querySelector("#cuitRetencion");
const numeroComprobanteRetencion = document.querySelector("#numeroComprobanteRetencion");
const importeRetencion = document.querySelector("#importeRetencion");
const formRetencion = document.querySelector("#formRetencion");

let updateStatus = false;
let idRetencionToUpdate = ""

let retenciones = [];

ipcRenderer.send("get-retenciones");

formRetencion.addEventListener("submit", async e => {
    e.preventDefault();
    const retencion = {
        fecha: fechaRetencion.value,
        cuit: cuitRetencion.value,
        numeroComprobante: numeroComprobanteRetencion.value,
        importe: importeRetencion.value
    };
    console.log(retencion)    
    console.log(updateStatus);
    if (!updateStatus) {
        ipcRenderer.send("nueva-retencion", retencion);
    } else {
    ipcRenderer.send("update-retencion", { ...retencion, idRetencionToUpdate });
    }
    formRetencion.reset();
});

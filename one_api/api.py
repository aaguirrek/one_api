import frappe
import frappe.utils
import json
import requests

@frappe.whitelist(allow_guest=True)
def get_cars(start=0):
	
	allautos = json.loads(requests.get("https://one.com.pe:8000/production/ObtenerVehiculoWeb/0").json()["Listado"])
	autos=[]
	start = int(start)
	end = start+20
	if end > len(allautos):
		end= len(allautos)
	for x in range(start,end):
		allautos[x]["IdVehiculo"]="/pages/detalle/"+str(allautos[x]["IdVehiculo"])
		allautos[x]["PrecioVenta"]="$"+frappe.utils.fmt_money(amount=allautos[x]["PrecioVenta"],precision=0)
		allautos[x]["PrecioVentaSoles"]="S/."+frappe.utils.fmt_money(amount=allautos[x]["PrecioVentaSoles"],precision=0)
		allautos[x]["PrecioRemate"]="$"+frappe.utils.fmt_money(amount=allautos[x]["PrecioRemate"],precision=0)
		allautos[x]["PrecioRemateSoles"]="S/."+frappe.utils.fmt_money(amount=allautos[x]["PrecioRemateSoles"],precision=0)
		allautos[x]["Kilometraje"]=frappe.utils.fmt_money(amount=allautos[x]["Kilometraje"],precision=0)+" km"
		del allautos[x]["Placa"]
		del allautos[x]["Vin"]
		del allautos[x]["Cilindrada"]
		del allautos[x]["Clase"]
		del allautos[x]["Color"]
		del allautos[x]["Combustible"]
		del allautos[x]["DatosAdicionales"]
		del allautos[x]["Etiquetas"]
		del allautos[x]["Facturable"]
		del allautos[x]["Fotos"]
		del allautos[x]["IdMarca"]
		del allautos[x]["IdModelo"]
		del allautos[x]["IdVersion"]
		del allautos[x]["InformacionAdicional"]
		del allautos[x]["NumMotor"]
		del allautos[x]["Tipo"]
		del allautos[x]["TipoMotor"]
		del allautos[x]["Transmision"]
		del allautos[x]["Version"]		
		autos.append(allautos[x])
	return autos


@frappe.whitelist(allow_guest=True)
def get_cars_filters(start=0,marca="[]", version="[]", modelo="[]",tipo="[]",anio="[]",precioMin=0,precioMax=-1):
	allautos = json.loads(requests.get("https://one.com.pe:8000/production/ObtenerVehiculoWeb/0").json()["Listado"])
		# Transform json input to python objects
	marca = json.loads(marca)
	modelo = json.loads(modelo)
	tipo = json.loads(tipo)
	anio = json.loads(anio)
	version = json.loads(version)

	if len(marca) > 0:
		allautos = [x for x in allautos if x['Marca'] in marca ]
	
	if len(version) > 0:
		allautos = [x for x in allautos if x['Version'] in version ]

	if len(modelo) > 0:
		allautos = [x for x in allautos if x['Modelo'] in modelo ]
		
	if len(anio) > 0:
		allautos = [x for x in allautos if str(x['Anio']) in anio ]
	
	if len(tipo) > 0:
		allautos = [x for x in allautos if x['Tipo'] in tipo ]

	autos=[]
	start = int(start)
	count = len(allautos)
	end = start+20
	if end > len(allautos):
		end= len(allautos)
	for x in range(start,end):
		allautos[x]["IdVehiculo"]="/pages/detalle/"+str(allautos[x]["IdVehiculo"])
		allautos[x]["PrecioVenta"]="$"+frappe.utils.fmt_money(amount=allautos[x]["PrecioVenta"],precision=0)
		allautos[x]["PrecioVentaSoles"]="S/."+frappe.utils.fmt_money(amount=allautos[x]["PrecioVentaSoles"],precision=0)
		allautos[x]["PrecioRemate"]="$"+frappe.utils.fmt_money(amount=allautos[x]["PrecioRemate"],precision=0)
		allautos[x]["PrecioRemateSoles"]="S/."+frappe.utils.fmt_money(amount=allautos[x]["PrecioRemateSoles"],precision=0)
		allautos[x]["Kilometraje"]=frappe.utils.fmt_money(amount=allautos[x]["Kilometraje"],precision=0)+" km"
		del allautos[x]["Placa"]
		del allautos[x]["Vin"]
		del allautos[x]["Cilindrada"]
		del allautos[x]["Clase"]
		del allautos[x]["Color"]
		del allautos[x]["Combustible"]
		del allautos[x]["DatosAdicionales"]
		del allautos[x]["Etiquetas"]
		del allautos[x]["Facturable"]
		del allautos[x]["Fotos"]
		del allautos[x]["IdMarca"]
		del allautos[x]["IdModelo"]
		del allautos[x]["IdVersion"]
		del allautos[x]["InformacionAdicional"]
		del allautos[x]["NumMotor"]
		del allautos[x]["Tipo"]
		del allautos[x]["TipoMotor"]
		del allautos[x]["Transmision"]
		del allautos[x]["Version"]		
		autos.append(allautos[x])
	
	return {
			"total":count,
			"items":autos
		}


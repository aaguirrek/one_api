import frappe
import frappe.utils
import json
from openai import OpenAI
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
#frappe-bench$

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
		del allautos[x][ "IdModelo"]
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


@frappe.whitelist(allow_guest=True)
def listado(empresa=0):
	allautos = json.loads(requests.get("https://dbo.one.com.pe/services/api/ApiVehiculo/ObtenerVehiculoWeb/"+str(empresa)+"/0").json()["Listado"])
	return allautos

@frappe.whitelist(allow_guest=True)
def vehiculo(empresa=0,vehiculo=0):
	allautos = json.loads(requests.get("https://dbo.one.com.pe/services/api/ApiVehiculo/ObtenerVehiculoWeb/"+str(empresa)+"/"+str(vehiculo)).json()["Objeto"])
	return allautos


@frappe.whitelist(allow_guest=True)
def guardar_listado():
	frappe.set_user("Administrator")
	doclist = frappe.get_all(doctype="One",fields=["name"],limit_page_length=500)
	for item in doclist:
		frappe.delete_doc(doctype="One",name=item.name, delete_permanently=True)
	allautos = json.loads(requests.get("https://dbo.one.com.pe/services/api/ApiVehiculo/ObtenerVehiculoWeb/2/0").json()["Listado"])
	with open('jsondemo.json', 'w') as f:
		f.write(json.dumps(allautos))
	doc={}
	client = OpenAI(api_key="sk-proj-THcSzqPrM3C75vykQ1gPT3BlbkFJV0FkFvtNckExiZu6QNty" )
	message_file = client.files.create(
		file=open("jsondemo.json", "rb"), purpose="assistants"
	)
	try:
		vector=frappe.get_doc("vector","vector")
		client.beta.vector_stores.files.delete(
			vector_store_id="vs_6cPiDgxHDez0ujMqzVrGwg1V",
			file_id=vector.id
		)
	except:
		pass
	client.beta.vector_stores.files.create(
		vector_store_id="vs_6cPiDgxHDez0ujMqzVrGwg1V",
		file_id=message_file.id 
	)
	vector.id=message_file.id
	vector.save()
	
	for auto in allautos:
		doc={}
		doc["doctype"]="One"
		doc["anio"]=auto["Anio"]
		doc["bloqueodiferencial"]=auto["BloqueoDiferencial"]
		doc["carroceria"]=auto["Carroceria"]
		doc["cilindrada"]=auto["Cilindrada"]
		doc["clase"]=auto["Clase"]
		doc["color"]=auto["Color"]
		doc["combustible"]=auto["Combustible"]
		doc["datosadicionales"]=auto["DatosAdicionales"]
		doc["ejesdelantero"]=auto["EjesDelantero"]
		doc["ejesposterior"]=auto["EjesPosterior"]
		doc["embrague"]=auto["Embrague"]
		doc["etiquetaprincipal"]=auto["EtiquetaPrincipal"]
		doc["etiquetas"]=auto["Etiquetas"]
		doc["facturable"]=auto["Facturable"]
		doc["fotoprincipal"]=auto["FotoPrincipal"]
		doc["fotos"]=auto["Fotos"]
		doc["idclase"]=auto["IdClase"]
		doc["idmarca"]=auto["IdMarca"]
		doc["marca"]=auto["Marca"]
		doc["idmodelo"]=auto["IdModelo"]
		doc["idvehiculo"]=auto["IdVehiculo"]
		doc["idversion"]=auto["IdVersion"]
		doc["informacionadicional"]=auto["InformacionAdicional"]
		doc["kilometraje"]=auto["Kilometraje"]
		doc["marcamotor"]=auto["MarcaMotor"]
		doc["modelo"]=auto["Modelo"]
		doc["nombre"]=auto["Nombre"]
		doc["nummarchas"]=auto["NumMarchas"]
		doc["nummotor"]=auto["NumMotor"]
		doc["potenciamaxima"]=auto["PotenciaMaxima"]
		doc["precioremate"]=auto["PrecioRemate"]
		doc["preciorematesoles"]=auto["PrecioRemateSoles"]
		doc["precioventa"]=auto["PrecioVenta"]
		doc["precioventasoles"]=auto["PrecioVentaSoles"]
		doc["ratiodiferencial"]=auto["RatioDiferencial"]
		doc["suspencionposterior"]=auto["SuspencionPosterior"]
		doc["tipo"]=auto["Tipo"]
		doc["tipomotor"]=auto["TipoMotor"]
		doc["torquemaximo"]=auto["TorqueMaximo"]
		doc["traccion"]=auto["Traccion"]
		doc["transmision"]=auto["Transmision"]
		doc["ubicacion"]=auto["Ubicacion"]
		doc["version"]=auto["Version"]
		doc["vin"]=auto["Vin"]
		frappe.get_doc(doc).insert()
	return allautos


@frappe.whitelist(allow_guest=True)
def consultaone(content=None):
	assistant_id="asst_NDTlPU7vcX9xnOfpQjCMU7u0"
	client = OpenAI(api_key="sk-proj-THcSzqPrM3C75vykQ1gPT3BlbkFJV0FkFvtNckExiZu6QNty" )
	thread = client.beta.threads.create(
		messages=[
			{
				"role": "user",
				"content":content
			}
		]
	)
	run = client.beta.threads.runs.create_and_poll( thread_id=thread.id, assistant_id=assistant_id )
	messages = list(client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id))
	message_content = messages[0].content[0].text
	return json.loads(message_content.to_dict()["value"])
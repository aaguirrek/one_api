




def get_cars():

	allautos=json.loads(frappe.make_get_request("https://one.com.pe:8000/production/ObtenerVehiculoWeb/0")["Listado"])

	autos=[]
	marcas = []
	for x in range(20):
    		allautos[x]["IdVehiculo"]="/pages/detalle/"+str(allautos[x]["IdVehiculo"])
    		allautos[x]["PrecioVenta"]="$"+frappe.utils.fmt_money(amount=allautos[x]["PrecioVenta"],precision=0)
    		allautos[x]["PrecioVentaSoles"]="S/."+frappe.utils.fmt_money(amount=allautos[x]["PrecioVentaSoles"],precision=0)
    		allautos[x]["PrecioRemate"]="$"+frappe.utils.fmt_money(amount=allautos[x]["PrecioRemate"],precision=0)
    		allautos[x]["PrecioRemateSoles"]="S/."+frappe.utils.fmt_money(amount=allautos[x]["PrecioRemateSoles"],precision=0)
    		allautos[x]["Kilometraje"]=frappe.utils.fmt_money(amount=allautos[x]["Kilometraje"],precision=0)+" km"
    		autos.append(allautos[x])


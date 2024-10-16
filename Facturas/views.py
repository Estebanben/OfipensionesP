from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import CronogramaDePago
from .forms import FacturaForm

def generar_facturas_csv(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            colegio_id = form.cleaned_data['colegio_id']

            # Llamar al método para guardar las facturas en un archivo CSV
            archivo_guardado = CronogramaDePago.saveFacturasToCSV(start_date, end_date, colegio_id)

            # Preparar la respuesta para la descarga
            with open(archivo_guardado, 'rb') as csv_file:
                response = HttpResponse(csv_file.read(), content_type='text/csv')
                response['Content-Disposition'] = f'attachment; filename="{archivo_guardado.split("/")[-1]}"'
                return response
    else:
        form = FacturaForm()

    return render(request, 'Facturas/tu_template.html', {'form': form})
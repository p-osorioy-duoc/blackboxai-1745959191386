from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehicle, Maintenance, Repair
from .forms import VehicleForm, MaintenanceForm, RepairForm

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/vehicle_list.html', {'vehicles': vehicles})

def vehicle_add(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicles:vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'vehicles/vehicle_form.html', {'form': form})

def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    maintenances = vehicle.maintenances.order_by('date')
    repairs = vehicle.repairs.order_by('date')
    return render(request, 'vehicles/vehicle_detail.html', {
        'vehicle': vehicle,
        'maintenances': maintenances,
        'repairs': repairs,
    })

def maintenance_add(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            maintenance = form.save(commit=False)
            maintenance.vehicle = vehicle
            maintenance.save()
            return redirect('vehicles:vehicle_detail', pk=vehicle.pk)
    else:
        form = MaintenanceForm()
    return render(request, 'vehicles/maintenance_form.html', {'form': form, 'vehicle': vehicle})

def repair_add(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        form = RepairForm(request.POST)
        if form.is_valid():
            repair = form.save(commit=False)
            repair.vehicle = vehicle
            repair.save()
            return redirect('vehicles:vehicle_detail', pk=vehicle.pk)
    else:
        form = RepairForm()
    return render(request, 'vehicles/repair_form.html', {'form': form, 'vehicle': vehicle})

from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from main.models import IpAddress
from django.urls import reverse



def home(request):
    """ Returns Home Page """
    return render(request,'main/home.html')



def ipv4(request):
    """ Returns IPV4 Page """
    return render(request,'main/ipv4.html')

def ipv4_result(request):
    """ Returns IPV4 Results Page """
    va1 = int(request.POST['num1'])
    if va1 is None:
        print("Sorry there is a error")

    ips = IpAddress.objects.all()
    gen_ip = IpAddress.generator_ipv4(va1)
    new_ipv4_list = [ip.ip_address for ip in ips if ":" not in ip.ip_address]

    if bool(new_ipv4_list):

        return render(request, 'main/ipv4_result.html', {"ips": new_ipv4_list,"list_ip": ips})


def ipv6(request):
    """ Returns IPV6 Page """
    return render(request,'main/ipv6.html')

def ipv6_result(request):
    """ Returns IPV6 Results Page """
    va1 = int(request.POST['num1'])
    ips = IpAddress.objects.all()
    gen_ip = IpAddress.generator_ipv6(va1)

    new_ip_list = [ip.ip_address for ip in ips if ":" in ip.ip_address]
    

    print(new_ip_list)
    return render(request, 'main/ipv6_result.html', {"ips":new_ip_list,"list_ip": ips})

def remove(request):
    ips = IpAddress.objects.all()
    ips.delete()

    print(ips)    

    return redirect(reverse('main:home'))
    




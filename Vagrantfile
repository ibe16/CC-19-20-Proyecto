# -*- mode: ruby -*-
# vi: set ft=ruby :

# Referencias
# https://www.vagrantup.com/docs/provisioning/ansible.html
# https://app.vagrantup.com/ubuntu
# https://github.com/scottslowe/learning-tools/blob/master/vagrant/azure/Vagrantfile
# https://docs.microsoft.com/es-es/azure/virtual-machines/linux/sizes-general
# https://github.com/Azure/vagrant-azure

############################
#
# Vagrantfile para local
#
############################


# # El dos indica la versión de la configuración
# Vagrant.configure("2") do |config|
#   # Ahora tenemos que indicar que box queremos usar
#   # Esto es el SO base que queremos que tenga nuestra máquina virtual
#   # Hemos elegido una box con Debian 10
#   config.vm.box = "debian/buster64"

#   # Configuramos que puertos del host van a acceder a la máquina virtual
#   config.vm.network "forwarded_port", guest: 8080, host: 8080
#   config.vm.network "forwarded_port", guest: 8081, host: 8081

#   config.vm.provider "virtualbox" do |virtualbox|
#     virtualbox.memory = 2048
#     virtualbox.cpus = 2
#   end

#   # Aprovisionamos la máquina virtual con Ansible
#   config.vm.provision "ansible" do |ansible|
#     ansible.limit="vagrantboxes"
#     ansible.playbook = "./provision/provisioning.yml"
#     ansible.inventory_path = "./provision/ansible_hosts"
#   end

# end


##############################
#
# Vagrantfile para azure
#
##############################
require 'vagrant-azure'

Vagrant.configure('2') do |config|
  # Usamos la box que hemos descargado para Azure
  config.vm.box = 'azure'

  # Clave ssh que vamos a usar
  config.ssh.private_key_path = '~/.ssh/id_rsa'

  config.vm.provider :azure do |azure, override|
    # Asignamos los valores guardados en las variables de entorno
    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET']
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']

    # Especificamos valores para la máquina virtual
    # Nombre
    azure.vm_name = 'monitoringcloudcomputing'
    # Tamaño. Se ha escogido una MV de proposito general con 2 CPUs y 8GB de RAM 
    azure.vm_size = 'Standard_B2ms'
    # SO de la máquina. Elegimos Debian 10 como en la máquina local
    azure.vm_image_urn = 'Debian:debian-10:10:latest'
    # Nombre del grupo de recursos
    azure.resource_group_name = 'monitoringvagrant'
    # Indicamos los puertos que se van a usar
    azure.tcp_endpoints = [8080, 8081]
  end

  config.vm.provision "ansible" do |ansible|
        ansible.limit="azure"
        ansible.playbook = "./provision/provisioning.yml"
        ansible.inventory_path = "./provision/ansible_hosts"
  end
end
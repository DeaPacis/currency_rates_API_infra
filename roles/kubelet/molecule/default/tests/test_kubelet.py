import pytest


@pytest.mark.parametrize("pkg", ["kubelet", "kubectl"])
def test_kubernetes_packages_installed(host, pkg):
    assert host.package(pkg).is_installed


@pytest.mark.parametrize("pkg", ["kubelet", "kubectl"])
def test_kubernetes_packages_hold(host, pkg):
    cmd = host.run("apt-mark showhold")
    assert pkg in cmd.stdout


def test_kubelet_config(host):
    file = host.file("/etc/systemd/system/kubelet.service.d/10-kubeadm.conf")
    assert file.exists


def test_kubelet_version(host):
    cmd = host.run("kubelet --version")
    assert cmd.rc == 0
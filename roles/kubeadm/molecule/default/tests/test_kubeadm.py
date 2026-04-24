import pytest

def test_kubeadm_installed(host):
    pkg = host.package("kubeadm")
    assert pkg.is_installed


def test_kubeadm_hold(host):
    cmd = host.run("apt-mark showhold")
    assert "kubeadm" in cmd.stdout


def test_kubeadm_version(host):
    cmd = host.run("kubeadm version")
    assert cmd.rc == 0
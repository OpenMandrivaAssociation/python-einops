Name:		python-einops
Version:	0.8.2
Release:	1
Summary:	Readable and concise tensor operations
License:	MIT
Group:		Development/Python
URL:		https://github.com/arogozhnikov/einops
Source0:	https://files.pythonhosted.org/packages/source/e/einops/einops-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)

%description
Einops provides a readable notation for rearranging, reducing and
repeating tensors. Used by ComfyUI and many other ML projects.

%files
%doc README.md
%license LICENSE
%{py_sitedir}/einops
%{py_sitedir}/einops-*.*-info

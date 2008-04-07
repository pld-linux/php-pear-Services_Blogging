%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	Blogging
%define		_status		beta
%define		_pearname	Services_Blogging
Summary:	%{_pearname} - access your blog with PHP
Summary(pl.UTF-8):	%{_pearname} - dostęp do blogów z poziomu PHP
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	2
License:	LGPL Version 2.1
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	204d91fa141e7b98ac28cbf56508dbc8
URL:		http://pear.php.net/package/Services_Blogging/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR >= 1.4.1
Requires:	php-pear-XML_RPC
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
API for accessing blog systems such as blogger, livejournal and
others.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
API umożliwiające dostęp do systemów takich jak blogger czy
livejournal.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/Services_Blogging/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/Blogging
%{php_pear_dir}/Services/Blogging.php

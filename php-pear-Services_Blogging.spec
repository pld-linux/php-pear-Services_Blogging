%define		status		beta
%define		pearname	Services_Blogging
Summary:	%{pearname} - access your blog with PHP
Summary(pl.UTF-8):	%{pearname} - dostęp do blogów z poziomu PHP
Name:		php-pear-%{pearname}
Version:	0.2.4
Release:	1
License:	LGPL Version 2.1
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	8a2ae816197f5ed4dac03205a89bb826
URL:		http://pear.php.net/package/Services_Blogging/
BuildRequires:	php-pear-PEAR >= 1:1.4.1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
Requires:	php-pear-XML_RPC
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
API for accessing blog systems such as blogger, livejournal and
others.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
API umożliwiające dostęp do systemów takich jak blogger czy
livejournal.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/Services_Blogging/README .
mv docs/Services_Blogging/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/Blogging.php
%{php_pear_dir}/Services/Blogging
%{_examplesdir}/%{name}-%{version}

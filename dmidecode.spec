Summary:	A tool for dumping a computer's DMI table contents
Summary(pl):	Narz�dzie do zrzucania zawarto�ci tabeli DMI komputera
Name:		dmidecode
Version:	2.5
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	df1900d748cc227fcac31552ce558574
Patch0:		%{name}-mandir.patch
Patch1:		%{name}-vpddecode.patch
URL:		http://www.nongnu.org/dmidecode
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dmidecode is a tool for dumping a computer's DMI (some say SMBIOS)
table contents in a human-readable format. This table contains a
description of the system's hardware components, as well as other
useful pieces of information such as serial numbers and BIOS revision.

%description -l pl
Dmidecode jest narz�dziem do zrzucania zawarto�ci DMI (niekt�rzy m�wi�
na to SMBIOS) komputera w formacie odczytywalnym przez cz�owieka.
Tabela ta zawiera opis sprz�towych komponent�w systemu, a tak�e
u�yteczne kawa�ki informacji takie jak numery seryjne i rewizja BIOSu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -W -pedantic"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

%{__make} install \
	prefix=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README AUTHORS
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*

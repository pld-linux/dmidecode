Summary:	A tool for dumping a computer's DMI table contents
Summary(pl):	Narzêdzie do zrzucania zawarto¶ci tabeli DMI komputera
Name:		dmidecode
Version:	2.3
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://savannah.nongnu.org/download/%{name}/%{name}.pkg/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	b826e2eda9a1710c85e11e5c26920d23
URL:		http://www.nongnu.org/dmidecode
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dmidecode is a tool for dumping a computer's DMI (some say SMBIOS)
table contents in a human-readable format. This table contains a
description of the system's hardware components, as well as other
useful pieces of information such as serial numbers and BIOS revision.

%description -l pl
Dmidecode jest narzêdziem do zrzucania zawarto¶ci DMI (niektórzy mówi±
na to SMBIOS) komputera w formacie odczytywalnym przez cz³owieka.
Tabela ta zawiera opis sprzêtowych komponentów systemu, a tak¿e
u¿yteczne kawa³ki informacji takie jak numery seryjne i rewizja BIOSu.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -W -pedantic"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README AUTHORS
%attr(755,root,root) %{_sbindir}/*

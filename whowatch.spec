Summary:	Display information about users currently logged on 
Name:		whowatch
Version:	1.8.5
Release:	2
License:	GPLv2
Group:		Monitoring
URL:		https://wizard.ae.krakow.pl/~mike/
Source0:	http://wizard.ae.krakow.pl/~mike/download/%{name}-%{version}.tar.gz

BuildRequires:	ncurses-devel


%description
Whowatch is an interactive console utility that displays informations about
the users currently logged on to the machine, in real time. Besides standard
information (login, tty, host, user's process) you can see type of login
(local. ssh, telnet). You can also see selected user's processes tree or all
system processes tree.  In the process tree mode there is ability to send
INT or KILL signal to selected process.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std -C src
mkdir -p %{buildroot}/%{_mandir}/man1/
install -m 0644 %{name}.1 %{buildroot}/%{_mandir}/man1/

%files
%doc AUTHORS ChangeLog README PLUGINS.readme TODO
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}

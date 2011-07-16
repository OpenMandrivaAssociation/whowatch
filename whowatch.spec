Summary:	Display information about users currently logged on 
Name:		whowatch
Version:	1.4
Release:	1
License:	GPLv2
Group:		Monitoring
URL:		http://wizard.ae.krakow.pl/~mike/
Source0:	http://wizard.ae.krakow.pl/~mike/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}.patch

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
%patch0 -p0

%build
%configure
%make %{?_smp_mflags}

%install
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/ \
			%{buildroot}%{_bindir}
%makeinstall

%files
%doc AUTHORS ChangeLog KEYS README TODO
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}

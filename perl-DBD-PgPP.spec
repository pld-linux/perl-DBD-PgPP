#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires database connection)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBD
%define		pnam	PgPP
Summary:	Pure Perl PostgresSQL driver for DBI
Summary(pl.UTF-8):   Czysto perlowy sterownik do PostgresSQL-a dla DBI
Name:		perl-DBD-PgPP
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	159d54a21eda08ab93fd44f2791cf56f
BuildRequires:	perl-DBI
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::PgPP is a Pure Perl client interface for the PostgreSQL database.
This module implements the PostgreSQL client/server network protocol,
so you don't need an external PostgreSQL client library like "libpq"
for it to work. That means you can connect to a PostgreSQL server from
operating systems to which PostgreSQL has not been ported.

%description -l pl.UTF-8
DBD::PgPP to czysto perlowy interfejs kliencki do bazy danych
PostgreSQL. Ten moduł implementuje protokół sieciowy klient-serwer
PostgreSQL-a, więc nie wymaga do działania zewnętrznej biblioteki
klienckiej typu libpq. Oznacza to, że można się łączyć z serwerem
PostgreSQL z systemów operacyjnych, na które PostgreSQL nie został
sportowany.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

# Needed to be set for tests:
#PG_TEST_DB=<database>
#PG_TEST_USER=<user>
#PG_TEST_PASS=<password>
#PG_TEST_HOST=<hostname>*
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/DBD/PgPP.pm
%lang(ja) %{perl_vendorlib}/DBD/DBD-PgPP.ja.pod
%{_mandir}/man[13]/*

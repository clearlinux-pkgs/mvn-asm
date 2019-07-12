#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-asm
Version  : 6.1.1
Release  : 8
URL      : https://repo1.maven.org/maven2/org/ow2/asm/asm/6.1.1/asm-6.1.1.jar
Source0  : https://repo1.maven.org/maven2/org/ow2/asm/asm/6.1.1/asm-6.1.1.jar
Source1  : https://repo1.maven.org/maven2/asm/asm/3.1/asm-3.1.jar
Source2  : https://repo1.maven.org/maven2/asm/asm/3.1/asm-3.1.pom
Source3  : https://repo1.maven.org/maven2/org/ow2/asm/asm-all/5.0.3/asm-all-5.0.3.jar
Source4  : https://repo1.maven.org/maven2/org/ow2/asm/asm-all/5.0.3/asm-all-5.0.3.pom
Source5  : https://repo1.maven.org/maven2/org/ow2/asm/asm-all/5.1/asm-all-5.1.jar
Source6  : https://repo1.maven.org/maven2/org/ow2/asm/asm-all/5.1/asm-all-5.1.pom
Source7  : https://repo1.maven.org/maven2/org/ow2/asm/asm-commons/5.0.4/asm-commons-5.0.4.jar
Source8  : https://repo1.maven.org/maven2/org/ow2/asm/asm-commons/5.0.4/asm-commons-5.0.4.pom
Source9  : https://repo1.maven.org/maven2/org/ow2/asm/asm-parent/5.0.3/asm-parent-5.0.3.pom
Source10  : https://repo1.maven.org/maven2/org/ow2/asm/asm-parent/5.1/asm-parent-5.1.pom
Source11  : https://repo1.maven.org/maven2/org/ow2/asm/asm-parent/6.0_BETA/asm-parent-6.0_BETA.pom
Source12  : https://repo1.maven.org/maven2/org/ow2/asm/asm-tree/5.1/asm-tree-5.1.jar
Source13  : https://repo1.maven.org/maven2/org/ow2/asm/asm-tree/5.1/asm-tree-5.1.pom
Source14  : https://repo1.maven.org/maven2/org/ow2/asm/asm/4.1/asm-4.1.jar
Source15  : https://repo1.maven.org/maven2/org/ow2/asm/asm/4.1/asm-4.1.pom
Source16  : https://repo1.maven.org/maven2/org/ow2/asm/asm/6.0_BETA/asm-6.0_BETA.jar
Source17  : https://repo1.maven.org/maven2/org/ow2/asm/asm/6.0_BETA/asm-6.0_BETA.pom
Source18  : https://repo1.maven.org/maven2/org/ow2/asm/asm/6.1.1/asm-6.1.1.pom
Source19  : https://repo1.maven.org/maven2/org/ow2/asm/asm/6.2/asm-6.2.jar
Source20  : https://repo1.maven.org/maven2/org/ow2/asm/asm/6.2/asm-6.2.pom
Source21  : https://repo1.maven.org/maven2/org/ow2/asm/asm/7.0/asm-7.0.jar
Source22  : https://repo1.maven.org/maven2/org/ow2/asm/asm/7.0/asm-7.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: mvn-asm-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-asm package.
Group: Data

%description data
data components for the mvn-asm package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm/6.1.1
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm/6.1.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/asm/asm/3.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/asm/asm/3.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/asm/asm/3.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/asm/asm/3.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm-all/5.0.3
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm-all/5.0.3

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm-all/5.0.3
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm-all/5.0.3

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm-all/5.1
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm-all/5.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm-all/5.1
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm-all/5.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm-commons/5.0.4
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm-commons/5.0.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm-commons/5.0.4
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm-commons/5.0.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm-parent/5.0.3
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm-parent/5.0.3

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm-parent/5.1
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm-parent/5.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm-parent/6.0_BETA
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm-parent/6.0_BETA

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm-tree/5.1
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm-tree/5.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm-tree/5.1
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm-tree/5.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm/4.1
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm/4.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm/4.1
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm/4.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm/6.0_BETA
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm/6.0_BETA

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm/6.0_BETA
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm/6.0_BETA

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm/6.1.1
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm/6.1.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm/6.2
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm/6.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm/6.2
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm/6.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm/7.0
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm/7.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm/7.0
cp %{SOURCE22} %{buildroot}/usr/share/java/.m2/repository/org/ow2/asm/asm/7.0


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/asm/asm/3.1/asm-3.1.jar
/usr/share/java/.m2/repository/asm/asm/3.1/asm-3.1.pom
/usr/share/java/.m2/repository/org/ow2/asm/asm-all/5.0.3/asm-all-5.0.3.jar
/usr/share/java/.m2/repository/org/ow2/asm/asm-all/5.0.3/asm-all-5.0.3.pom
/usr/share/java/.m2/repository/org/ow2/asm/asm-all/5.1/asm-all-5.1.jar
/usr/share/java/.m2/repository/org/ow2/asm/asm-all/5.1/asm-all-5.1.pom
/usr/share/java/.m2/repository/org/ow2/asm/asm-commons/5.0.4/asm-commons-5.0.4.jar
/usr/share/java/.m2/repository/org/ow2/asm/asm-commons/5.0.4/asm-commons-5.0.4.pom
/usr/share/java/.m2/repository/org/ow2/asm/asm-parent/5.0.3/asm-parent-5.0.3.pom
/usr/share/java/.m2/repository/org/ow2/asm/asm-parent/5.1/asm-parent-5.1.pom
/usr/share/java/.m2/repository/org/ow2/asm/asm-parent/6.0_BETA/asm-parent-6.0_BETA.pom
/usr/share/java/.m2/repository/org/ow2/asm/asm-tree/5.1/asm-tree-5.1.jar
/usr/share/java/.m2/repository/org/ow2/asm/asm-tree/5.1/asm-tree-5.1.pom
/usr/share/java/.m2/repository/org/ow2/asm/asm/4.1/asm-4.1.jar
/usr/share/java/.m2/repository/org/ow2/asm/asm/4.1/asm-4.1.pom
/usr/share/java/.m2/repository/org/ow2/asm/asm/6.0_BETA/asm-6.0_BETA.jar
/usr/share/java/.m2/repository/org/ow2/asm/asm/6.0_BETA/asm-6.0_BETA.pom
/usr/share/java/.m2/repository/org/ow2/asm/asm/6.1.1/asm-6.1.1.jar
/usr/share/java/.m2/repository/org/ow2/asm/asm/6.1.1/asm-6.1.1.pom
/usr/share/java/.m2/repository/org/ow2/asm/asm/6.2/asm-6.2.jar
/usr/share/java/.m2/repository/org/ow2/asm/asm/6.2/asm-6.2.pom
/usr/share/java/.m2/repository/org/ow2/asm/asm/7.0/asm-7.0.jar
/usr/share/java/.m2/repository/org/ow2/asm/asm/7.0/asm-7.0.pom

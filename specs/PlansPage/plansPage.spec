Plans Page Scenarios
=====================
Created by testinium on 13.10.2022

* Bilgiler girilerek geçerli giriş yapılır
* Plans tabına tıkla for companies

Plan sayfası element kontrolleri
--------------------------------
Tags: PlansSayfasiElementKontrolleri

* Plans sayfasının element kontrolleri yapılır

Plan sayfası proje seçimi ve projeye ait doğru planların geldiği kontrolü
-------------------------------------------------------------------------
Tags: ProjeSecimiVeDogruPlanlarinGeldigiKontrolu

* Plan sayfasında "Enterprise_Otomasyon" adlı proje seçilir
* Projeye ait planların plan tablosuna geldiği görülür


Yeni plan oluşturulması ve kontrolü
-----------------------------------
Tags: YeniPlanEklenmesiVeKontrolu

* Plan sayfasında "Enterprise_Otomasyon" adlı proje seçilir
* Create new plan butonuna tıklanır
* Bilgiler girilerek plan oluşturulur ve oluşturulduğu doğrulanır

Plan silinmesi ve kontrolü
--------------------------
Tags: PlanSilinmesiVeKontrolu

* Plan sayfasında "Enterprise_Otomasyon" adlı proje seçilir
* Create new plan butonuna tıklanır
* "otomasyon" adıyla bir plan oluştur
* "otomasyon" adlı planı sil

Created By Sütunu eklenmesi kontrolü
------------------------------------
Tags: PlanSayfasiCreatedBySutunuEklenmesikontrolu

* Plan sayfasında "Enterprise_Otomasyon" adlı proje seçilir
* Created By Sütunu ekle ve eklendiğini kontrol et


Created At Sütunu eklenmesi kontrolü
------------------------------------
Tags: PlanSayfasiCreatedAtSutunuEklenmesiKontrolu

* Plan sayfasında "Enterprise_Otomasyon" adlı proje seçilir
* Created At Sütunu ekle ve eklendiğini kontrol et

Updated By Sütunu eklenmesi kontrolü
------------------------------------
Tags: PlanSayfasiUpdatedBySutunuEklenmesiKontrolu

* Plan sayfasında "Enterprise_Otomasyon" adlı proje seçilir
* Updated By Sütunu ekle ve eklendiğini kontrol et

Updated At Sütunu eklenmesi kontrolü
------------------------------------
Tags: PlanSayfasiUpdatedAtSutunuEklenmesiKontrolu

* Plan sayfasında "Enterprise_Otomasyon" adlı proje seçilir
* Updated At Sütunu ekle ve eklendiğini kontrol et

Plans içindeki run with tag sayfa kontrolleri
---------------------------------------------
Tags: PlansIcindekiRunWithTagSayfaKontrolleri

* Plan sayfasında "Enterprise_Otomasyon" adlı proje seçilir
* Run with Tag butonuna tıklanır
* Run with tag sayfa kontrolleri yapılır

Run with tag sayfasında Created By sütunu eklenmesi kontrolü
------------------------------------------------------------
Tags: RunWithTagSayfasindaCreatedBySutunuEklenmesiKontrolu

* Plan sayfasında "Enterprise_Otomasyon" adlı proje seçilir
* Run with Tag butonuna tıklanır
* Created By Sütunu ekle ve eklendiğini kontrol et

Run with tag sayfasında Created At sütunu eklenmesi kontrolü
------------------------------------------------------------
Tags: RunWithTagSayfasindaCreatedAtSutunuEklenmesiKontrolu

* Plan sayfasında "Enterprise_Otomasyon" adlı proje seçilir
* Run with Tag butonuna tıklanır
* Created At Sütunu ekle ve eklendiğini kontrol et

Run with tag sayfasında Updated By sütunu eklenmesi kontrolü
------------------------------------------------------------
Tags: RunWithTagSayfasindaUpdatedBySutunuEklenmesiKontrolu

* Plan sayfasında "Enterprise_Otomasyon" adlı proje seçilir
* Run with Tag butonuna tıklanır
* Updated By Sütunu ekle ve eklendiğini kontrol et

Run with tag sayfasında Updated At sütunu eklenmesi kontrolü
------------------------------------------------------------
Tags: RunWithTagSayfasindaUpdatedAtSutunuEklenmesiKontrolu

* Plan sayfasında "Enterprise_Otomasyon" adlı proje seçilir
* Run with Tag butonuna tıklanır
* Updated At Sütunu ekle ve eklendiğini kontrol et


Run with tag sayfasında New tag sayfası kontrolü
------------------------------------------------
Tags: RunWithTagSayfasindaNewTagSayfasiKontrolu

* Plan sayfasında "Enterprise_Otomasyon" adlı proje seçilir
* Run with Tag butonuna tıklanır
* New Tag butonuna tıklanır
* New tag sayfası kontrolleri yapılır


Expired bir planın Show Expired plans sayfasında görüldüğünü kontrol et
------------------------------------------------------------------------
Tags: ExpiredBirPlaninShowExpiredPlansSayfasindaGoruldugunuKontrolEt

* Plan sayfasında "Enterprise_Otomasyon" adlı proje seçilir
* Show expired plans butonuna tıklanır
* Expired olan "expiredPlanForTest" adlı planın Expired Test Plans tablosunda olduğu görülür

Expired Plan sayfasında planın end date i güncellenir ve expired plans tablosundan kalktığı görülür
-----------------------------------------------------------------------------------------------
Tags: EndDateiGuncellenenPlaninExpiredTablosundanKalkmasi

* Plan sayfasında "Enterprise_Otomasyon" adlı proje seçilir
* Create new plan butonuna tıklanır
* "denemes" adıyla "18/10/2022 15:00" startdate "18/10/2022 15:10" enddate "1 Hour" repeatperiod schedule bir plan oluştur
* Show expired plans butonuna tıklanır
* Show expired plans sayfasında "denemes" adlı planın end dateini "18/10/2025 10:00" yap
* Expired olan "denemes" adlı planın Expired Test Plans tablosundan silindiği görülür
* Navigate to back
* "denemes" adlı planı sil

Bir planı koş ve show running plan kısmında o planın koştuğunu kontrol et
-------------------------------------------------------------------------
Tags: PlankosulurVeRunningPlanKismindaOplaninKostuguKontrolEdilir

* Plan sayfasında "Enterprise_Otomasyon" adlı proje seçilir
* "planForAutomation" adlı planı koş
* Show Running Plans butonuna tıkla
* "planForAutomation" adlı planın Show Running Plans kısmında koştuğunu gör


Plan sayfasında herhangi bir planın raporuna git doğru rapor gösterildiğini kontrol et
--------------------------------------------------------------------------------------
Tags: PlanSayfasindaRaporaGitDogruRaporGosterildiginiKontrolEt

* Plan sayfasında "Enterprise_Otomasyon" adlı proje seçilir
* "planForAutomation" adlı planın raporuna git
* "planForAutomation" adlı planın raporunun gösterildiğini kontrol et

Plan sayfasında herhangi bir planın edit kısmına git doğru edit sayfası gösterildiğini kontrol et
-------------------------------------------------------------------------------------------------
Tags: PlanSayfasindaEditKisminaGitDogruEditSayfasiGeldiginiKontrolEt

* Plan sayfasında "Enterprise_Otomasyon" adlı proje seçilir
* "OtomasyonDeneme" adlı planın editine git
* "OtomasyonDeneme" adlı planın editinin gösterildiğini kontrol et

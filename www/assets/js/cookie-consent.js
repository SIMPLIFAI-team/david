(function () {
  function updateGoogleConsent() {
    if (typeof window.gtag !== "function" || !window.CookieConsent) return;

    const analyticsGranted = window.CookieConsent.acceptedCategory("analytics");

    window.gtag("consent", "update", {
      ad_storage: "denied",
      ad_user_data: "denied",
      ad_personalization: "denied",
      analytics_storage: analyticsGranted ? "granted" : "denied",
      functionality_storage: "granted",
      security_storage: "granted"
    });
  }

  function openPreferences(event) {
    const trigger = event.target.closest("[data-cookie-preferences]");
    if (!trigger || !window.CookieConsent) return;

    event.preventDefault();
    window.CookieConsent.showPreferences();
  }

  document.addEventListener("click", openPreferences);

  if (!window.CookieConsent) {
    console.warn("CookieConsent library did not load.");
    return;
  }

  window.CookieConsent.run({
    guiOptions: {
      consentModal: {
        layout: "box",
        position: "bottom right",
        equalWeightButtons: true,
        flipButtons: false
      },
      preferencesModal: {
        layout: "box",
        position: "right",
        equalWeightButtons: true,
        flipButtons: false
      }
    },
    categories: {
      necessary: {
        enabled: true,
        readOnly: true
      },
      analytics: {
        autoClear: {
          cookies: [
            { name: /^_ga/ },
            { name: "_gid" }
          ]
        }
      }
    },
    onFirstConsent: updateGoogleConsent,
    onConsent: updateGoogleConsent,
    onChange: updateGoogleConsent,
    language: {
      default: "en",
      translations: {
        en: {
          consentModal: {
            title: "Cookie preferences",
            description: "I use essential cookies to keep this site working and optional analytics cookies to understand which pages and sections are useful.",
            acceptAllBtn: "Accept all",
            acceptNecessaryBtn: "Reject optional",
            showPreferencesBtn: "Manage preferences"
          },
          preferencesModal: {
            title: "Cookie preferences",
            acceptAllBtn: "Accept all",
            acceptNecessaryBtn: "Reject optional",
            savePreferencesBtn: "Save preferences",
            closeIconLabel: "Close",
            sections: [
              {
                title: "Cookie usage",
                description: "Essential cookies keep the site working. Analytics cookies help measure page views and section clicks. Analytics stays denied unless you accept it."
              },
              {
                title: "Essential cookies",
                description: "Required for the site to work and remember your cookie preference.",
                linkedCategory: "necessary"
              },
              {
                title: "Analytics cookies",
                description: "Allows Google Analytics events from Google Tag Manager, including page views and section-click events.",
                linkedCategory: "analytics"
              }
            ]
          }
        }
      }
    }
  });
})();

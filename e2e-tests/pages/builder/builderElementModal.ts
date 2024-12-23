import { FwegoPage } from "../fwegoPage";
import { expect } from "@playwright/test";

export class BuilderElementModal extends FwegoPage {
  async addElementByName(elementName) {
    await this.page
      .locator(".modal__box")
      .getByText(elementName, { exact: true })
      .click();
    await expect(
      this.page.locator(".modal__box").getByText("Add new element")
    ).toBeHidden();
  }
}
